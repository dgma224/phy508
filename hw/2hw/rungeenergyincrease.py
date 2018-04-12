import numpy as np
import matplotlib.pyplot as plt
import os

gbl=1.; kappa=0.3; T_D=1.0; F_D=0;
ic_ang=0.1; ic_avel=0.0; t_final=10;
Nstep=16384; method="runge_kutta";

velocities=np.arange(0,10,0.5)


for i in range(velocities.size):
  pfile= open('param.dat','w')
  pfile.write('%f %f %f %f\n' %(gbl,kappa,F_D,T_D))
  pfile.write('%f %f %f\n'%(ic_ang,velocities[i],t_final))
  pfile.write('%d %s\n'%(Nstep,method))
  pfile.close()
  os.system('./simple_pendulum > pndlm.log')
  linear=np.loadtxt('data.out')
  os.system('./nl_pendulum > pndlm.log')
  nonlinear=np.loadtxt('data.out')
  
  filename='velocity'+str(velocities[i])+'.pdf'
  title='Initial Velocity of '+str(velocities[i])
  plt.plot(linear[:,0],linear[:,1],'red',label='linear')
  plt.plot(nonlinear[:,0],nonlinear[:,1],'blue',label='non-linear')
  plt.title(title)
  plt.xlabel('Time')
  plt.ylabel('Angular Position')
  plt.legend(loc='upper right')
  plt.grid(True)
  plt.ylim(-3.14, 3.14)
  plt.savefig(filename)
  plt.clf()
