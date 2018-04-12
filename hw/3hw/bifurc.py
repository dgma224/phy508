#This Python code will create the bifurcation diagram used for Problem 2 of this assignment

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

pi=3.1415
#setup base param file
perTD=100 #number of steps per T_D
numberofTD=1100 #number of driving force periods to run for
gbl=1.; kappa=0.5; T_D=3.0*pi; F_D=0;
ic_ang=0.0; ic_avel=0.0; t_final=T_D*numberofTD;
Nstep=numberofTD*perTD; method="runge_kutta";
#number of values at end of Nstep to keep
#y part of the graph
ycol=1
numtoplot = 100 #number of values per F_D to plot

#setup range of F_D values
fd=np.arange(1.025,1.125,0.0005)
lastang=0.0
lastvel=0.0
for i in range(fd.size):
  #create parameter file with this
  pfile= open('param.dat','w')
  pfile.write('%f %f %f %f\n' %(gbl,kappa,fd[i],T_D))
  pfile.write('%f %f %f\n'%(lastang,lastvel,t_final))
  pfile.write('%d %s\n'%(Nstep,method))
  pfile.close()
  os.system('./nl_pendulum > pndlm.log')
  #read in data file, figure out where to start reading
  firstval=perTD*(numberofTD-numtoplot-1);
  lastval=perTD*(numberofTD-1)
  datapd=pd.read_table('data.out',sep=' ')
  data=datapd.as_matrix()
  ydat=data[firstval:lastval:perTD,ycol]
  #setup repeating xvalues for the plot
  xvals=np.full_like(ydat,fd[i])
  plt.scatter(xvals,ydat,s=1)
  #setup last values for next run 
  lastang=data[-1,1]
  lastvel=data[-1,2]
plt.xlabel('F_D')
plt.ylabel('Final Angular Position')
plt.title('Bifurcation Diagram for Angular Position')
plt.show()
