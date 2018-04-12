import matplotlib.pyplot as plt
import numpy as np
import sys
import os

size = np.arange(10,120,5)
prob = np.arange(0.56,0.62,0.01)
nclust=1
nbin=1000
seed=10
bound='sqlatt_OBC'

averages = np.zeros(len(size))
for j in range(len(prob)):
  for i in range(len(size)):
    pfile=open('param.dat','w')
    pfile.write('%d %f %d %d %d %s\n' %(size[i],prob[j],nclust,nbin,seed,bound))
    pfile.close()
    os.system('./perc_hw > log.log')
    data = np.loadtxt('data.out')
    averages[i]=np.mean(data)
  plt.plot(size,averages,label=''+str(prob[j]*100)+' percent')
 
plt.xlabel('Size of Lattice')
plt.ylabel('Average Percent in Cluster')
plt.title('Lattice Size vs Size of Cluster')
plt.legend(loc='upper left')
plt.show()
