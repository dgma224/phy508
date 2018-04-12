import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import time
#set range of sizes of lattice
startsize = 9
stopsize = 10
numsteps=stopsize+1-startsize
sizes=np.logspace(startsize, stopsize,num=numsteps,base=2)
startprob=0.575
stopprob=0.6
stepprob=0.001
probs=np.arange(startprob,stopprob,stepprob)
nclust=10
nbin=100
seed=10
bound='sqlatt_OBC'

#what column to plot
ycol=3

averages=np.zeros(len(probs))
errors=np.zeros(len(probs))
for j in range(len(sizes)):
  for i in range(len(probs)):
  
    pfile=open('param.dat','w')
    pfile.write('%d %f %d %d %d %s\n' %(sizes[j],probs[i],nclust,nbin,seed,bound))
    pfile.close()
    start = time.time()
    os.system('./perc_hw > log.log')
    print(str(sizes[j])+' : '+str(probs[i])+' : '+str(time.time()-start))

    data = np.loadtxt('data.out')
    averages[i]=np.mean(data[:,ycol])
    errors[i]=np.std(data[:,ycol])
  plt.errorbar(probs, averages,xerr=0.0,yerr=errors,label='size='+str(sizes[j]))
plt.legend(loc='upper right')
plt.xlabel('Probability of Cluster Growth')
plt.ylabel('Probability of Percolation')
plt.show()
