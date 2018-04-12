#include <stdio.h>
#include "MersenneTwister.h"
#include <fstream>
#include <stdlib.h>
using namespace std;

int main(int argc, char *argv[]){
  if(argc<4){
    cout<<"Improper Inputs Given"<<endl;
    cout<<"Expected: ./clt SEED Number_Obs, NumReps"<<endl;
    return 0;
  }
  int SEED = atoi(argv[1]);
  int Nobs = atoi(argv[2]);
  int numhist = atoi(argv[3]);


  MTRand ran1(SEED);
  ofstream dfout;
  dfout.open("data.out");

  float xave = 0.0;

  for(int j = 0;j<numhist;j++){
    for(int i = 0;i<Nobs;i++){
      xave+=ran1.rand();
    }
    dfout<<xave/((float)Nobs)<<endl;
    xave=0.0f;
  }
  dfout.close();
  return 0;
}
