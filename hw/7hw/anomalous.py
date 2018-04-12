import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import time
prs=[0.4,0.595,0.7]
startsize=10
stopsize=200
stepsize=5
sizes=np.arange(startsize,stopsize,stepsize)
nclust=10
nbin=100
seed=10
bound='sqlatt_OBC'
ycol=0

#curve fitting function
def func(x,a,b,c):
  return a*x**(b)+c
averages=np.zeros(len(sizes))
errors=np.zeros(len(sizes))
for i in range(len(prs)):
  for j in range(len(sizes)):
    pfile=open('param.dat','w')
    pfile.write('%d %f %d %d %d %s\n' %(sizes[j],prs[i],nclust,nbin,seed,bound))
    pfile.close()
    start = time.time()
    os.system('./perc_hw > log.log')
    print(str(sizes[j])+' : '+str(prs[i])+' : '+str(time.time()-start))
    data=np.loadtxt('data.out')
    averages[j]=np.mean(data[:,ycol])
    errors[j]=np.std(data[:,ycol])
  print(averages)
  plt.errorbar(sizes, averages, xerr=0.0, yerr=errors,label='pr= '+str(prs[i]))
  #do curve fitting
  param,blah=curve_fit(func,sizes,averages,bounds=(0,[1000,3,1000]))
  print(param)
  plt.plot(sizes,func(sizes,param[0],param[1],param[2]))

plt.legend(loc='upper right')
plt.xscale("log",basex=2)
plt.yscale("log",basey=2)
plt.xlabel('Size of Lattice')
plt.ylabel('Average Size of Cluster')
plt.show()
  
