#This python code will create the plots for Part A of the assignment

import numpy as np
import matplotlib.pyplot as plt
import os

pi=3.1415
#setup base param file
gbl=1.; kappa=0.5; T_D=2.0*pi/(2.0/3.0); F_D=0;
ic_ang=0.1; ic_avel=0.0; t_final=100;
Nstep=100000; method="runge_kutta";
transrange=Nstep-50000
#define some values
velocities=np.arange(0,6,2)
positions=np.arange(0,pi,pi/3.0)
xcol=1;ycol=2;

#do initial plot with no driving force
pfile= open('param.dat','w')
pfile.write('%f %f %f %f\n' %(gbl,kappa,F_D,T_D))
pfile.write('%f %f %f\n'%(ic_ang,ic_avel,t_final))
pfile.write('%d %s\n'%(Nstep,method))
pfile.close()
os.system('./nl_pendulum > pndlm.log')
original=np.loadtxt('data.out')
plt.plot(original[:,xcol],original[:,ycol],label='No F_D')

#now setup driving force for the future
F_D=0.1
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
  plt.plot(adjusted[transrange:,xcol],adjusted[transrange:,ycol],label=legendlabel)
plt.title('F_D = 0.0 and 0.1')

xlow=-0.5;
xhigh=0.5;
ylow=-0.5;
yhigh=0.5;
plt.xlim(xlow,xhigh)
plt.ylim(ylow,yhigh)
plt.xlabel('Angular Position')
plt.ylabel('Angular Velocity')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('apart.png')
plt.show()

