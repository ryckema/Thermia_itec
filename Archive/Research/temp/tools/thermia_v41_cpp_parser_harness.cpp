#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <vector>

using Bytes = std::vector<uint8_t>;

static uint16_t crc16(const uint8_t* data, size_t len) {
  uint16_t crc=0xFFFF;
  for(size_t i=0;i<len;i++){
    crc ^= data[i];
    for(int b=0;b<8;b++) crc=(crc&1)?uint16_t((crc>>1)^0xA001):uint16_t(crc>>1);
  }
  return crc;
}
static bool crc_ok(const Bytes& b, size_t len) {
  if(len<5 || b.size()<len) return false;
  uint16_t got=uint16_t(b[len-2]) | (uint16_t(b[len-1])<<8);
  return crc16(b.data(),len-2)==got;
}
static bool known_slave(uint8_t s){
  return s==0x01||s==0x02||s==0x03||s==0x04||s==0x05||s==0x06||
         s==0x0A||s==0x0F||s==0x14||s==0x1E||s==0xA4||s==0xA5||s==0xC8;
}
static bool known_fn(uint8_t f){
  return f==0x01||f==0x02||f==0x03||f==0x04||f==0x05||f==0x06||
         f==0x08||f==0x0F||f==0x10||f==0x16||f==0x17||(f&0x80);
}
static std::vector<size_t> candidates(const Bytes& p){
  std::vector<size_t> c;
  if(p.size()<2) return c;
  uint8_t fn=p[1];
  if(fn&0x80) c.push_back(5);
  if(fn==0x01||fn==0x02){
    c.push_back(8);
    if(p.size()>=3 && p[2]<=240) c.push_back(5+size_t(p[2]));
  }
  if(fn==0x05||fn==0x06||fn==0x08) c.push_back(8);
  if(fn==0x0F){
    c.push_back(8);
    if(p.size()>=7 && p[6]<=240) c.push_back(9+size_t(p[6]));
  }
  if(fn==0x16) c.push_back(10);
  if(fn==0x03||fn==0x04){
    c.push_back(8);
    if(p.size()>=3 && p[2]<=240) c.push_back(5+size_t(p[2]));
  }
  if(fn==0x10){
    c.push_back(8);
    if(p.size()>=7 && p[6]<=240) c.push_back(9+size_t(p[6]));
  }
  if(fn==0x17){
    if(p.size()>=3 && p[2]<=240) c.push_back(5+size_t(p[2]));
    if(p.size()>=11 && p[10]<=240) c.push_back(13+size_t(p[10]));
  }
  std::sort(c.begin(),c.end());
  c.erase(std::unique(c.begin(),c.end()),c.end());
  return c;
}

struct Parser {
  Bytes pending;
  std::vector<Bytes> frames;
  uint64_t resync=0,drops=0;

  void feed(const uint8_t* data,size_t n){
    pending.insert(pending.end(),data,data+n);
    if(pending.size()>4096){drops++;pending.clear();return;}
    while(true){
      if(pending.size()<5) break;
      uint8_t slave=pending[0],fn=pending[1];
      if(!known_slave(slave)||!known_fn(fn)){
        pending.erase(pending.begin()); continue;
      }
      auto c=candidates(pending);
      size_t matched=0; bool waiting=false;
      for(size_t len:c){
        if(len<5||len>256) continue;
        if(pending.size()<len){waiting=true;continue;}
        if(crc_ok(pending,len)){matched=len;break;}
      }
      if(matched){
        frames.emplace_back(pending.begin(),pending.begin()+matched);
        pending.erase(pending.begin(),pending.begin()+matched);
        continue;
      }
      if(waiting) break;
      resync++;
      pending.erase(pending.begin());
    }
    if(pending.size()>512){drops++;pending.clear();}
  }
};

static Bytes hex2bytes(const std::string& s){
  Bytes b;
  for(size_t i=0;i+1<s.size();i+=2){
    unsigned v=0;
    std::stringstream ss; ss<<std::hex<<s.substr(i,2); ss>>v;
    b.push_back(uint8_t(v));
  }
  return b;
}
static std::string hex(const Bytes& b){
  std::ostringstream os; os<<std::uppercase<<std::hex<<std::setfill('0');
  for(auto x:b) os<<std::setw(2)<<unsigned(x);
  return os.str();
}
static Bytes add_crc(Bytes b){
  uint16_t c=crc16(b.data(),b.size());
  b.push_back(uint8_t(c&0xFF)); b.push_back(uint8_t(c>>8)); return b;
}
static bool semantic_req(const Bytes& b){
  if(b.size()!=8||b[0]!=0x0F||b[1]!=0x03||!crc_ok(b,b.size())) return false;
  uint16_t st=(uint16_t(b[2])<<8)|b[3], ct=(uint16_t(b[4])<<8)|b[5];
  return (st==0x03E8&&ct==14)||(st==0x042E&&ct==15)||
         (st==0x0442&&ct==13)||(st==0x0546&&ct==20);
}
static Bytes ambiguous0546(){
  Bytes p={0x0F,0x03,0x05,0x46,0x00,0x14};
  uint16_t c=crc16(p.data(),p.size());
  p.push_back(uint8_t(c&0xFF));p.push_back(uint8_t(c>>8));
  return add_crc(p);
}
static Bytes find_bc4(uint16_t st,uint16_t ct){
  for(int x=0;x<256;x++){
    Bytes p={0x0F,0x03,0x04,uint8_t(st&0xFF),uint8_t(ct>>8),uint8_t(ct&0xFF),uint8_t(x)};
    Bytes full=add_crc(p);
    Bytes pref(full.begin(),full.begin()+8);
    if(semantic_req(pref)) return full;
  }
  return {};
}

int main(int argc,char**argv){
  if(argc<2){std::cerr<<"fixture required\n";return 2;}
  std::ifstream in(argv[1]);
  if(!in){std::cerr<<"cannot open fixture\n";return 2;}
  std::vector<Bytes> expected;
  std::string line;
  while(std::getline(in,line)){
    if(line.empty()||line[0]=='#') continue;
    expected.push_back(hex2bytes(line));
  }

  int pass=0;
  for(int run=0;run<50;run++){
    Parser p; std::mt19937 rng(0x700000u+run);
    for(const auto& fr:expected){
      size_t pos=0;
      while(pos<fr.size()){
        size_t n=1+(rng()%31); n=std::min(n,fr.size()-pos);
        p.feed(fr.data()+pos,n); pos+=n;
      }
    }
    bool ok=(p.frames==expected && p.pending.empty());
    if(ok) pass++;
  }

  std::vector<std::pair<std::string,Bytes>> adv={
    {"042E",find_bc4(0x042E,15)},
    {"0442",find_bc4(0x0442,13)},
    {"0546",ambiguous0546()}
  };
  int whole_short=0, split_short=0;
  for(auto& [name,fr]:adv){
    Parser p1; p1.feed(fr.data(),fr.size());
    if(!p1.frames.empty() && semantic_req(p1.frames.front()) && p1.frames.front().size()==8) whole_short++;

    Parser p2; p2.feed(fr.data(),8); p2.feed(fr.data()+8,fr.size()-8);
    if(!p2.frames.empty() && semantic_req(p2.frames.front()) && p2.frames.front().size()==8) split_short++;

    std::cout<<"ADV "<<name<<" full="<<hex(fr)
             <<" first="<<(p1.frames.empty()?"":hex(p1.frames.front()))
             <<" pending="<<p1.pending.size()<<"\n";
  }

  std::cout<<"CPP_PARSER_HARNESS\n";
  std::cout<<"genuine_frames="<<expected.size()<<"\n";
  std::cout<<"genuine_chunk_runs_pass="<<pass<<"/50\n";
  std::cout<<"adversarial_whole_short_prefix="<<whole_short<<"/3\n";
  std::cout<<"adversarial_split_short_prefix="<<split_short<<"/3\n";

  if(pass!=50 || whole_short!=3 || split_short!=3) return 1;
  return 0;
}