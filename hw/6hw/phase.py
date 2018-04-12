import matplotlib.pyplot as plt
import numpy as np
import sys
import os

size=200
probs = np.arange(0,1.0,0.01)
nclust=1
nbin=1000
seed=10
bound='sqlatt_PBC'

averages = np.zeros(len(probs))
for i in range(len(probs)):
  pfile=open('param.dat','w')
  pfile.write('%d %f %d %d %d %s\n' %(size,probs[i],nclust,nbin,seed,bound))
  pfile.close()
  os.system('./perc_hw > log.log')
  data = np.loadtxt('data.out')
  averages[i]=np.mean(data)/(size*size)
 
plt.plot(probs, averages)
plt.xlabel('Probability of Joining Cluster')
plt.ylabel('Average Percent in Cluster')
plt.title('Probability vs Average Size of Cluster')
plt.show()
