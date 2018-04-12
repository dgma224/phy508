#include <fstream> 
#include <iostream> 
#include <math.h>
#include <string>
#include <sstream>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include "MersenneTwister.h"

using namespace std;

class PARAMS
{
public:
  int Nlin; // linear size of lattice
  double pr; // probability for a site
  int Nclust; // number of clusters in a bin
  int Nbin; // number of bins of data to output
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
  double prob_perc_x;
  double prob_perc_y;
  double prob_perc;
  ofstream dfout;
};

int main(void)
{
  PARAMS p;
  LATTICE latt(p);
  CLUSTER cluster(p,latt);
  MTRand ran1(p.SEED);

  //latt.print();
  for (int bin=0;bin<p.Nbin;bin++){
    cluster.meas_clear(latt);
    for(int clust=0;clust<p.Nclust;clust++){
      cluster.grow(latt,ran1);
      cluster.meas(latt);
    }
    cluster.binwrite(p,latt);
    //cluster.print(latt,bin);
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
  //0 is not asked, 1 is asked and joined, 2 is asked and declined
  int askd = 0;
  int join = 1;
  int decl = 2;
  //clear and set conf to 0
  conf.clear();
  conf.resize(latt.Nsite,askd);

  //determine starting location
  int startloc = ran1.randInt(latt.Nsite-1);
  conf.at(startloc) = join;

  //initialize the stack
  stack.resize(latt.Nsite,askd);
  stack.at(0) = startloc;
  stck_end=1;//one element by default
  stck_pnt=0;
  while(stck_pnt<stck_end){//keep going until this is beyond
    //check each neighbor of the stack
    for(int i = 0;i<latt.nrnbrs.at(stack.at(stck_pnt)).size();i++){
      //get neighbor location
      int neigh = latt.nrnbrs.at(stack.at(stck_pnt)).at(i);
      if(conf.at(neigh)==decl || conf.at(neigh)==join){
        //do nothing if they've been asked before
      }
      else if(ran1.rand()<pr){//asked and joined 
        stack.at(stck_end) = neigh;
        stck_end++;//add one more to the stack
        conf.at(neigh) = join;
      }
      else{//asked and declined
        conf.at(neigh)=decl;
      }
    }
    //print(latt,stck_pnt); //used for debugging  
    stck_pnt+=1;//now shift up the list
  }
  size = stck_end; //set size of cluster to number of values in stack
}

void CLUSTER::print(const LATTICE& latt, int index)
{

  stringstream ss;
  string file_name;
  ss<<"./plots/"<<index<<".clust";
  file_name=ss.str();

  ofstream clout;
  clout.open(file_name.c_str());
  //clout <<"#"<<latt.Lx<<" x "<<latt.Ly<<endl;
 
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
  //now determine if it percolated now
  //check bottom side
  bool bottest = false;
  bool toptest = false;
  bool lefttest = false;
  bool righttest = false;
  int Lx = latt.Lx;
  int i = 0;
  while(i<Lx && bottest==false){
    if(conf.at(i)==1)
      bottest=true;
    i++;
  }
  i=0;
  while(i<Lx && toptest==false){
    if(conf.at(Lx*Lx-1-i)==1)
      toptest=true;
    i++;
  }
  i=0;
  while(i<Lx && lefttest==false){
    if(conf.at(Lx*i)==1)
      lefttest = true;
    i++;
  }
  i=0;
  while(i<Lx && righttest==false){
    if(conf.at(Lx*(i+1)-1)==1)
      righttest = true;
    i++;
  }
  if(bottest==true && toptest==true)
    prob_perc_y+=1.0;
  if(lefttest==true && righttest==true)
    prob_perc_x+=1.0;
  if((lefttest==true && righttest==true) || (bottest==true && toptest==true))
    prob_perc+=1.0;
}


void CLUSTER::meas_clear(const LATTICE& latt)
{
  avg_size=0.;
  prob_perc=0.;
  prob_perc_x=0.;
  prob_perc_y=0.;
}


void CLUSTER::binwrite(const PARAMS& p, const LATTICE& latt)
{
  dfout << avg_size/((double)p.Nclust)<<" "<<prob_perc_x/((double)p.Nclust);
  dfout << " "<<prob_perc_y/((double)p.Nclust)<<" "<<prob_perc/((double)p.Nclust)<<endl;
}
