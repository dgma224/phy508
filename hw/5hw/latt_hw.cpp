#include <fstream> 
#include <iostream> 
#include <math.h>
#include <string>
#include <iomanip>
#include <vector>
#include <cstdlib>

using namespace std;

class PARAMS
{
public:
  int Nlin; // size of cluster
  double pr; // probability for a site
  double Nclust; // number of clusters in a bin
  double Nbin; // number of bins of data to output
  int SEED; // seed for mersenne twister
  string latt_; // which lattice 
  PARAMS();//constructor
};

class LATTICE
{
public:
  LATTICE(const PARAMS&);//constructor
  int Nsite;// number of lattice sites
  int Lx,Ly;
  vector<vector<int> > nrnbrs;
  void print ();
  string latt_;
};



int main(void)
{
  PARAMS p;
  LATTICE latt(p);

  latt.print();
  
}

PARAMS::PARAMS(){
  //initializes commonly used parameters from a file
  ifstream pfin;
  pfin.open("param.dat");  
  if (pfin.is_open()) { 
    pfin >> Nlin;
    pfin >> pr;
    pfin >> Nclust;
    pfin >> Nbin;
    pfin >> SEED;
    pfin >> latt_;
  }
  else
    {cout << "No input file to read ... exiting!"<<endl;exit(1);}
  pfin.close();
  // print out all parameters for record
  cout << "--- Parameters at input for percolation problem ---"<<endl; 
  cout <<"Nlin = "<<Nlin<<"; prob. of site = "<<pr<<endl;
  cout <<"Number of clusters in a bin = "<<Nclust<<"; Number of bins = "<<Nbin<<endl;
  cout <<"RNG will be given SEED of = "<<SEED<<endl;
  cout <<"Percolation problem on lattice --> "<<latt_<<endl;
  
};//constructor


LATTICE::LATTICE (const PARAMS& p)
{

  latt_=p.latt_;

  if(p.latt_=="sqlatt_PBC")
    {
      Lx=p.Nlin;Ly=p.Nlin;
      Nsite=Lx*Ly;
      //resize neighbor vector
      nrnbrs.resize(Nsite);
      for(int x = 0;x<Lx;x++){
        for(int y = 0;y<Ly;y++){
          //lower x neighbor
          nrnbrs.at(x+y*Lx).push_back((x-1+Lx)%Lx + y*Lx);
          //higher x neigbhor
          nrnbrs.at(x+y*Lx).push_back((x+1)%Lx + y*Lx);
          //lower y neighbor
          nrnbrs.at(x+y*Lx).push_back(x + (y-1+Ly)%Ly*Lx);
          //higher y neighbor
          nrnbrs.at(x+y*Lx).push_back(x + (y+1)%Ly*Lx);
        }
      }
          
    }
  else if(p.latt_=="sqlatt_OBC")
    {
      Lx=p.Nlin;Ly=p.Nlin;
      Nsite=Lx*Ly;
      //resize neighbor vector
      nrnbrs.resize(Nsite);
      for(int x = 0;x<Lx;x++){
        for(int y = 0;y<Ly;y++){
          if(x-1>=0)//lower x neighbor
            nrnbrs.at(x+y*Lx).push_back(x-1+y*Lx);
          if(x+1<Lx)//higher x neighbor
            nrnbrs.at(x+y*Lx).push_back(x+1+y*Lx);
          if(y-1>=0)//lower y neighbor
            nrnbrs.at(x+y*Lx).push_back(x+(y-1)*Lx);
          if(y+1<Ly)//higher y neighbor
            nrnbrs.at(x+y*Lx).push_back(x+(y+1)*Lx);
        }
      }
          
    }
  else
    {cout <<"Dont know your option for lattice in param.dat .. exiting"<<endl;exit(1);}
}

void LATTICE::print()
{
  //THIS FUNCTIONS MAY BE CALLED DURING DEBUGGING TO MAKE SURE LATTICE HAS BEEN DEFINED CORRECTLY
  // DO NOT MODIFY
  cout <<"---printing out properties of lattice ---"<<endl;
  cout<<"size is  "<<Lx<<"x"<<Ly<<endl;
  cout <<"neighbors are"<<endl;
  for (int site=0;site<Nsite;site++)
    {
      cout <<site<<" : [nn of nbrs = "<<nrnbrs.at(site).size()<<"] which are  ";
      for (int nn=0;nn<nrnbrs.at(site).size();nn++)
	cout<<nrnbrs.at(site).at(nn)<<" ";
      cout <<endl;
    }
}
