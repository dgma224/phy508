#include <fstream> 
#include <iostream> 
#include <math.h>
#include <string>
#include <sstream>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include "MersenneTwister.h"
x1
using namespace std;

class PARAMS
{
public:
  int Nlin; // linear size of lattice
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

};

class CLUSTER
{
public:
  CLUSTER(const PARAMS&, const LATTICE&);//constructor
  void grow(const LATTICE&, MTRand&);
  void meas_clear(const LATTICE&);
  void meas(const LATTICE&);
  void binwrite(const PARAMS&, const LATTICE&);
  void print(const LATTICE& latt, int index);
  ~CLUSTER();// destructor
private:
  int size;
  vector <int> conf;
  vector <int> stack;
  double pr;
  int stck_pnt,stck_end;
  double avg_size;
  ofstream dfout;
 
};

int main(void)
{
  PARAMS p;
  LATTICE latt(p);
  CLUSTER cluster(p,latt);
  MTRand ran1(p.SEED);

  //latt.print();
  for (int bin=0;bin<p.Nbin;bin++)
    {
      cluster.meas_clear(latt);
      for(int clust=0;clust<p.Nclust;clust++)
	{
	  cluster.grow(latt,ran1);
	  cluster.meas(latt);

	}
      cluster.binwrite(p,latt);
    }
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
  // COMPLETE HERE
}

void LATTICE::print()
{
  //THIS FUNCTIONS MAY BE CALLED DURING DEBUGGING TO MAKE SURE LATTICE HAS BEEN DEFINED CORRECTLY
  cout <<"---printing out properties of lattice ---"<<endl;
  cout<<"size is  "<<Lx<<"x"<<Ly<<endl;
  cout <<"neighbors are"<<endl;
  for (int site=0;site<Nsite;site++)
    {
      cout <<site<<" : ";
      for (int nn=0;nn<nrnbrs.at(site).size();nn++)
	cout<<nrnbrs.at(site).at(nn)<<" ";
      cout <<endl;
    }
}


CLUSTER::CLUSTER(const PARAMS& p, const LATTICE& latt)
{
  conf.resize(latt.Nsite);
  stack.resize(latt.Nsite);
  pr=p.pr;// store prob in a private member of cluster
  dfout.open("data.out");
}

CLUSTER::~CLUSTER()
{
  dfout.close();
}

void CLUSTER::grow(const LATTICE& latt, MTRand& ran1)
{
  // COMPLETE HERE !!

}

void CLUSTER::print(const LATTICE& latt, int index)
{

  stringstream ss;
  string file_name;
  ss<<index<<".clust";
  file_name=ss.str();

  ofstream clout;
  clout.open(file_name.c_str());
  clout <<"#"<<latt.Lx<<" x "<<latt.Ly<<endl;
 
  for (int y=0;y<latt.Ly;y++)
    {
      for (int x=0;x<latt.Lx;x++)
	clout<<conf[x+y*latt.Lx]<<" ";
      clout<<endl;
    }
      
  clout.close();
}

void CLUSTER::meas(const LATTICE& latt)
{
  avg_size+=(double)size;
}


void CLUSTER::meas_clear(const LATTICE& latt)
{
  avg_size=0.;
}


void CLUSTER::binwrite(const PARAMS& p, const LATTICE& latt)
{
  dfout << avg_size/((double)p.Nclust)<<endl;
}
