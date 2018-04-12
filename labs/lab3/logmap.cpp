#include <iostream>
#include <math.h>
#include <fstream>
#include <stdlib.h>
using namespace std;

int main (void)
{
  double x, x_init;
  int Nmax;
  double r;

  // read param.dat
  ifstream pfin;
  pfin.open("param.dat");  
  if (pfin.is_open()) { 
  pfin>>r;
  pfin>>x_init;
  pfin>>Nmax;
  }
  else
    {cout << "No input file to read ... exiting!"<<endl;exit(1);}
  pfin.close();
  

  
  ofstream dfout;
  dfout.open("data.out"); 
  x=x_init;
  dfout<<x<<endl;
  for(int iter=0;iter<Nmax;iter++)
    {
      x=4.*r*x*(1.-x);
      dfout<<x<<endl;
    }
  dfout.close();

  return(1);
}

