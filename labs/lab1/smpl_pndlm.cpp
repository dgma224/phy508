#include <fstream> 
#include <iostream> 
#include <math.h>
#include <string>
#include <iomanip>
#include <stdlib.h>
using namespace std;

class PARAMS
{
public:
  double gbl;
  double kappa;
  double F_D;
  double T_D;
  double ic_ang;
  double ic_avel;
  double t_final;  
  int Nstep;
  string method;
  PARAMS();//constructor
};

class PROPAGATE
{
public:
  double dt;
  double pi;
  double ang,avel,time;
  ofstream dfout;
  PROPAGATE(const PARAMS&);//constructor
  void euler(const PARAMS&);
  void euler_cromer(const PARAMS&);
  void runge_kutta(const PARAMS&);
  void step(const PARAMS&);
  void print(const PARAMS&);
  ~PROPAGATE();
private:
  double avel_new,ang_new;
};

// MAIN PROGRAM
int main(void)
{
  PARAMS param;
  PROPAGATE prop(param);

  prop.print(param);  
  for(int step=0;step<param.Nstep;step++)
    {
      prop.step(param);
      prop.print(param);
    }
  
}// END MAIN PROGRAM


PARAMS::PARAMS(){
  //initializes commonly used parameters from a file
  ifstream pfin;
  pfin.open("param.dat");  
  if (pfin.is_open()) { 
    pfin >> gbl;
    pfin >> kappa;
    pfin >> F_D;
    pfin >> T_D;
    pfin >> ic_ang;
    pfin >> ic_avel;
    pfin >> t_final;
    pfin >> Nstep;
    pfin >> method;
  }
  else
    {cout << "No input file to read ... exiting!"<<endl;exit(1);}
  pfin.close();
  // print out all parameters for record
  cout << "--- Parameters at input for pendulum program ---"<<endl; 
  cout <<"g/l = "<<gbl<<"; kappa = "<<kappa<<"; F_D = "<<F_D<<"; T_D = "<<T_D<<endl;
  cout <<"init angle = "<<ic_ang<<"; init vel = "<<ic_avel<<"; t_final = "<<t_final<<endl;
  cout <<"Nstep = "<<Nstep<<"; method = "<<method<<endl;
  cout <<"natural time period ="<<8.*atan(1.)/sqrt(gbl)<<endl;
};//constructor

PROPAGATE::PROPAGATE(const PARAMS& p){
    dt=p.t_final/(double)p.Nstep;
    pi=4.*atan(1.);
    ang=p.ic_ang;
    avel=p.ic_avel;
    time=0.;
    dfout.open("data.out"); // clears data.out
   };//constructor

void PROPAGATE::euler(const PARAMS& p){
  // COMPLETE IN NEXT LAB
  cout <<"not coded in yet"<<endl;exit(1);

};

void PROPAGATE::euler_cromer(const PARAMS& p){

  avel=avel-(p.gbl*ang+p.kappa*avel)*dt; 
  ang=ang+avel*dt;  
  time+=dt;
};

void PROPAGATE::runge_kutta(const PARAMS& p){
  // COMPLETE IN HW 
  cout <<"not coded in yet"<<endl;exit(1);
};

void PROPAGATE::step(const PARAMS& p){
  
  //INEFFECIENT. IMPROVE LATER ....

  if (p.method=="euler")
      euler(p);
    else if (p.method=="euler_cromer")
      euler_cromer(p);
    else if (p.method=="runge_kutta")
      runge_kutta(p);
    else
      {cout <<"dont know which option you want ... exiting!"<<endl;exit(1);}
};

void PROPAGATE::print(const PARAMS& p){
    double energy=p.gbl*(1.-cos(ang))+avel*avel/2.;/*in units of ml^2*/
    dfout<<setprecision(10) <<time<<" "<<ang<<" "<<avel<<" "<<energy<<endl;
};

PROPAGATE::~PROPAGATE()
{
  dfout.close();
};

