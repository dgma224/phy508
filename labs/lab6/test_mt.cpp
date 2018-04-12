#include <stdio.h>
#include "MersenneTwister.h"
#include <fstream>
using namespace std;

int main (void)
{

  int SEED; // should be same as unsigned int


  //PART I
  cout << "enter SEED:"<<endl;  
  cin >> SEED;

  MTRand ran1 (SEED);
  cout <<"ran1"<<endl;
  for (int i=0;i<10;i++)
    cout <<ran1.randInt(4)<<endl;

  // even a slightly different seed gives a completely different sequence
  MTRand ran2 (SEED+1); 
  cout <<"ran2"<<endl;
  for (int i=0;i<10;i++)
    cout <<ran2.randInt(10)<<endl;


  //PART II
  int Nobs;
  cout <<"enter # of observations:"<<endl;
  cin >> Nobs;
  ofstream dfout;
  dfout.open("data.out");
  for (int obs=0;obs<Nobs;obs++)
    dfout << ran2.rand()<<endl;
  dfout.close();

}

