#include <fstream> 
#include <iostream> 
#include <math.h>
#include <string>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <sstream>
#include "MersenneTwister.h"

using namespace std;

class PARAMS
{
public:
  int Nlin; // linear size of lattice
  double beta; // 1/T
  int Neql;// eql sweeps
  int Nmcs;// sweeps in a bin
  int Nbin;// number of bin
  int SEED; // for MT
  string latt_;// lattice kind
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

class ISING_CONF
{
public:
  ISING_CONF(const PARAMS&, const LATTICE&, MTRand&);//constructor
  void conf_write(const PARAMS&, const LATTICE& latt,int index);
  void sweep(const PARAMS&,const LATTICE&,MTRand&);
  void meas_clear(const PARAMS&,const LATTICE&,MTRand&);
  void meas(const PARAMS&,const LATTICE&,MTRand&);
  void binwrite(const PARAMS&,const LATTICE&,MTRand&);
  ~ISING_CONF();// destructor
private:
  vector <int> spin;
  ofstream dfout;
  vector <vector<vector<double> > > wght_tbl;
  // these are the observables
  double energy;
  double energy_sq;
  double mag;
  double mag_sq;
};

int main(void)
{
  PARAMS p;
  LATTICE latt(p);
  MTRand ran1(p.SEED);
  ISING_CONF ising(p,latt,ran1);
  //ising.conf_write(p,latt);
  //latt.print();
  //EQUILIBRATE
  for(int eql=0;eql<p.Neql;eql++){
     ising.sweep(p,latt,ran1);
  }
  //PRODUCTION
   for (int bin=0;bin<p.Nbin;bin++)
     {
       ising.meas_clear(p,latt,ran1);
       for(int mcs=0;mcs<p.Nmcs;mcs++)
	 {
	    ising.sweep(p,latt,ran1);
	    ising.meas(p,latt,ran1);
	 }
       ising.binwrite(p,latt,ran1);
       //ising.conf_write(p,latt,bin);
     }
}

PARAMS::PARAMS(){
  ifstream pfin;
  pfin.open("param.dat");  
  if (pfin.is_open()) { 
    pfin >> Nlin;
    pfin >> beta;
    pfin >> Neql;
    pfin >> Nmcs;
    pfin >> Nbin;
    pfin >> SEED;
    pfin >> latt_;
  }
  else
    {cout << "No input file to read ... exiting!"<<endl;exit(1);}
  pfin.close();
  // print out all parameters for record
  cout << "--- Parameters at input for percolation problem ---"<<endl; 
  cout <<"Nlin = "<<Nlin<<"; beta = "<<beta<<endl;
  cout <<"# of equillibrium sweeps = "<<Neql<<"; # of Sweeps/bin = "<<Nmcs<<endl;
  cout <<"# of bins =  "<<Nbin<<"; SEED = "<<SEED<<endl;
  cout <<"Lattice Type = "<<latt_<<endl;
};//constructor


LATTICE::LATTICE (const PARAMS& p)
{
  if(p.latt_=="sqlatt_PBC")
    {
      Lx=p.Nlin;Ly=p.Nlin;
      Nsite=Lx*Ly;
      //resize neighbor vector
      nrnbrs.resize(Nsite);
      for(int x = 0;x<Lx;x++){
        for(int y = 0;y<Ly;y++){
          //higher x neigbhor
          nrnbrs.at(x+y*Lx).push_back((x+1)%Lx + y*Lx);
          //higher y neighbor
          nrnbrs.at(x+y*Lx).push_back(x + (y+1)%Ly*Lx);
          //lower y neighbor
          nrnbrs.at(x+y*Lx).push_back(x + (y-1+Ly)%Ly*Lx);
          //lower x neighbor
          nrnbrs.at(x+y*Lx).push_back((x-1+Lx)%Lx + y*Lx);
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


ISING_CONF::ISING_CONF(const PARAMS& p, const LATTICE& latt, MTRand& ran1)
{
  //first assign random values of either 0 or 1
  dfout.open("data.out");
  spin.resize(p.Nlin*p.Nlin);
  for(int i = 0;i<p.Nlin*p.Nlin;i++){
    spin.at(i)=ran1.randInt(1);
  }
  //CREATE WEIGHT TABLE
  if(p.latt_=="sqlatt_PBC")
    {
      //weight table, first index is sigma old
      //second index is sigma new
      //third index is sum of surrounding indices
      //first resize vector
      wght_tbl.resize(2);
      for(int i = 0;i<2;i++){
        wght_tbl.at(i).resize(2);
        for(int j = 0;j<2;j++){
          wght_tbl.at(i).at(j).resize(5);
        }
      }
      //now iterate through this mess and calculate each value
      for(int i = 0;i<2;i++){
        for(int j = 0;j<2;j++){
          for(int k = 0;k<5;k++){
            wght_tbl.at(i).at(j).at(k)=exp(2.0*p.beta*(j-i)*(2.0*k-4.0));
          }
        }
      }
      
    }
  else
    {cout <<"NEED TO CODE ALL LATTICE OPTIONS"<<endl;}
}

ISING_CONF::~ISING_CONF()
{
  dfout.close();
}

void ISING_CONF::conf_write(const PARAMS& p, const LATTICE& latt, int index)
{
  stringstream ss;
  string file_name;
  ss<<"./movie/conf"<<index<<".spin";
  file_name=ss.str();

  ofstream confout;
  confout.open(file_name.c_str());
  for(int i = 0;i<p.Nlin*p.Nlin;i++){
    if(i%p.Nlin == 0 && i!=0){
      confout<<endl;
    }
    confout<<spin.at(i)<<" ";
  }
  confout<<endl;
  confout.close();
}


void ISING_CONF::sweep(const PARAMS& p, const LATTICE& latt, MTRand& ran1)
{
  /*SWEEP THROUGH THE LATTICE*/
  for(int i = 0;i<p.Nlin*p.Nlin;i++){
    //determine the sum of the neighbors
    int sum = 0;
    for(int j = 0;j<latt.nrnbrs.at(i).size();j++){
      sum+=spin.at(latt.nrnbrs.at(i).at(j));
    }
    double ratio = wght_tbl.at(spin.at(i)).at(-1*spin.at(i)+1).at(sum);
    if(ratio>1.0){//accept this change
      spin.at(i)=-1*spin.at(i)+1;
    }
    else{
      if(ran1.rand()<ratio){
        spin.at(i)=-1*spin.at(i)+1;
      }
    }
  }
}

void ISING_CONF::meas_clear(const PARAMS& p, const LATTICE& latt, MTRand& ran1)
{
  energy=0.;
  energy_sq=0.;
  mag=0.;
  mag_sq=0.;
}

void ISING_CONF::meas(const PARAMS& p, const LATTICE& latt, MTRand& ran1)
{
  //remember spin array is 0 and 1, needs to be -1 and 1
  double tempmag=0;
  double tempener=0;
  for(int i =0;i<spin.size();i++){
    //right neighbor energy
    tempener+= (2.0*spin.at(i)-1.0)*(2.0*spin.at(latt.nrnbrs.at(i).at(0))-1.0);
    //upper neighbor energy
    tempener+= (2.0*spin.at(i)-1.0)*(2.0*spin.at(latt.nrnbrs.at(i).at(1))-1.0);
    //magnetization
    tempmag+=2.0*spin.at(i)-1.0;
  }
  double size=spin.size();
  mag+=tempmag/(size);
  energy+=-1.0*tempener/(size);
  mag_sq+=tempmag*tempmag/(size*size);
  energy_sq+=tempener*tempener/(size*size);  
}

void ISING_CONF::binwrite(const PARAMS& p, const LATTICE& latt, MTRand& ran1)
{
  mag=mag/(double(p.Nmcs));
  energy=energy/(double(p.Nmcs));
  mag_sq=mag_sq/(double(p.Nmcs));
  energy_sq=energy_sq/(double(p.Nmcs));
  dfout<<energy<<" "<<energy_sq<<" "<<mag<<" "<<mag_sq<<endl;  
}

