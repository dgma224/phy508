#this python code will create the plots for Part A of the assignment

import numpy as np
import matplotlib.pyplot as plt
import os

pi=3.1415
#setup base param file
numtd=1000
pertd=50
endvals=4*pertd
gbl=1.; kappa=0.5; T_D=2.0*pi/(2.0/3.0); F_D=0;
ic_ang=0.1; ic_avel=0.0; t_final=numtd*T_D;
Nstep=numtd*pertd; method="runge_kutta";

at=500 #only want the final few periods for this, get rid of transient

#do initial plot with no driving force
forces=[0.0,1.06,1.075,1.081,1.2]


for i in range(len(forces)):
  pfile= open('param.dat','w')
  pfile.write('%f %f %f %f\n' %(gbl,kappa,forces[i],T_D))
  pfile.write('%f %f %f\n'%(ic_ang,ic_avel,t_final))
  pfile.write('%d %s\n'%(Nstep,method))
  pfile.close()
  os.system('./nl_pendulum > pndlm.log')
  original=np.loadtxt('data.out')
 
  t=original[at*pertd:,0]
  angs=original[at*pertd:,1]
  vels=original[at*pertd:,2]
  xvals=np.arange(0,len(angs))
  fftangs=np.fft.fft(angs)
  fftvels=np.fft.fft(vels)
   
  absang=np.abs(fftangs)/len(angs)
  absvel=np.abs(fftvels)/len(angs)
  #roll over arrays to make image clearer
  absang=np.roll(absang, int(len(angs)/2.0))
  absvel=np.roll(absvel, int(len(angs)/2.0))
  xvals=np.arange(-1.0*len(angs)/2.0, len(angs)/2.0, 1.0)
  plt.plot(xvals,absang, color='r')
  plt.xlabel('Rolled over Index')
  plt.ylabel('Amplitude')
  plt.title('Force = '+str(forces[i]))
  plt.show()
  plt.clf()
  plt.plot(t[-endvals:],angs[-endvals:])
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.show()
