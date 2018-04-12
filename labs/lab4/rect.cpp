#include <iostream>
#include <string>
using namespace std;

class CRectangle {
public:
  int ln,br;
  string color;
  CRectangle();//constructor
  CRectangle(int,int,string);//constructor
  int area();// computes area of rectangle
  void print(); // prints out area and color
};


int main () {

  CRectangle rect1;
  CRectangle rect2(2,2,"blue");

  rect1.print();

  rect1.ln=8;
  rect1.color="green";

  rect1.print();

  rect2.print();
  
  return 0;
}


CRectangle::CRectangle()
{
  ln=1;
  br=1;
  color="white";
}//constructor                                                       

CRectangle::CRectangle(int x, int y, string col)
{
  ln=x;
  br=y;
  color=col;
}//constructor                                   

int CRectangle::area()
{
  return ln*br;
}

void CRectangle::print()
{  
  cout <<"Rectangle Properties"<<endl; 
  cout <<"Area: "<< area()<<endl;
  cout <<"Color: "<< color<<endl<<endl;
}

