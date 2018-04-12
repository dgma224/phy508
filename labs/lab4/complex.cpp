#include <iostream>
#include <math.h>

using namespace std;

class COMPLEX{
public:
  float real, imag;
  COMPLEX();//constructor
  COMPLEX(float, float);
  float abs();
  float arg();
  void print();
};

int main(){
  COMPLEX complex1;
  COMPLEX complex2(4.5,8.1);
  cout << complex2.abs()<<endl;
  cout << complex2.arg()<<endl;
  complex1.print();
  complex2.print();
  return 0;
}

COMPLEX::COMPLEX(){
  real=1;
  imag=0;
}

COMPLEX::COMPLEX(float r, float c){
  real=r;
  imag=c;
}

void COMPLEX::print(){
  cout<<real<<" + i*"<<imag<<endl;
}

float COMPLEX::abs(){
  return sqrt(real*real+imag*imag);
}

float COMPLEX::arg(){
  return atan(imag/real);
}
