#This python code will create the plots for Part A of the assignment

import numpy as np
import matplotlib.pyplot as plt
import os

pi=3.1415
#setup base param file
gbl=1.; kappa=0.5; T_D=2*pi/(2.0/3.0); F_D=0;
ic_ang=0.1; ic_avel=0.0; t_final=10000;
Nstep=16384*2*2*2*2*2; method="runge_kutta";
#define some values
pi=3.1415
at=4000; #values after transient
velocities=np.arange(0,6,2)
positions=np.arange(0,pi,pi/3.0)
xcol=1;ycol=2;

#now setup driving force for the future
F_D=1.2
#generate values for different starting locations
for i in range(velocities.size):
  pfile= open('param.dat','w')
  pfile.write('%f %f %f %f\n' %(gbl,kappa,F_D,T_D))
  pfile.write('%f %f %f\n'%(positions[i],velocities[i],t_final))
  pfile.write('%d %s\n'%(Nstep,method))
  pfile.close()
  os.system('./nl_pendulum > pndlm.log')
  adjusted=np.loadtxt('data.out')
  legendlabel=r'$\vartheta_0=$'+str(int(positions[i]))+' $\omega_0=$'+str(int(velocities[i]))
  plt.scatter(adjusted[Nstep-at:,xcol],adjusted[Nstep-at:,ycol],label=legendlabel,s=5)
  
  plt.title('F_D = '+str(F_D))
  plt.xlabel('Angular Position')
  plt.ylabel('Angular Velocity')
  plt.legend(loc='upper right')
  plt.grid(True)
  plt.show()
#these lines is included to remove the transient part
#plt.xlim(40,50)
#plt.ylim(-0.05,0.05)


