#This python code will create the plots for Part A of the assignment

import numpy as np
import matplotlib.pyplot as plt
import os

pi=3.1415
#setup base param file
perTD=100
numTD=100
gbl=1.; kappa=0.5; T_D=2*pi/(2.0/3.0); F_D=1.075;
ic_ang=0.1; ic_avel=0.0; t_final=numTD*T_D;
Nstep=int(t_final*perTD); method="runge_kutta";

at=30 #T_D to plot
atend=at*perTD

velocities=np.arange(0,6,2)
positions=np.arange(0,pi,pi/3.0)
xcol=1;ycol=2;

F_D=[1.06, 1.075, 1.081]

#generate values for different starting locations
for j in range(3):
  for i in range(velocities.size):
    pfile= open('param.dat','w')
    pfile.write('%f %f %f %f\n' %(gbl,kappa,F_D[j],T_D))
    pfile.write('%f %f %f\n'%(positions[i],velocities[i],t_final))
    pfile.write('%d %s\n'%(Nstep,method))
    pfile.close()
    os.system('./nl_pendulum > pndlm.log')
    data=np.loadtxt('data.out')

    legendlabel=r'$\vartheta_0=$'+str(int(positions[i]))+' $\omega_0=$'+str(int(velocities[i]))

    plt.scatter(data[Nstep-atend:,xcol],data[Nstep-atend:,ycol],label=legendlabel,s=5)

  plt.title('F_D = '+str(F_D[j]))
  plt.xlabel('Angular Position')
  plt.ylabel('Angular Velocity')
  plt.legend(loc='upper right')
  plt.grid(True)
  plt.savefig('f_d'+str(F_D[j])+'.pdf')
  plt.show()
  plt.clf()



