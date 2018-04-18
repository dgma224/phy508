#m2 plot script
#setup parameters here
import numpy as np
import matplotlib.pyplot as plt
import os 
import sys
import time

Betas=[0.440687,0.8,0.6,0.2,0.01]
Nlins=np.logspace(1,3,num=5,base=10)/2
Neql=1000
Nbin=1000
Nmcs=10
SEED=10
method='sqlatt_PBC'

#going to create one plot per beta
for i in range(len(Betas)):
  m2vals=np.zeros(len(Nlins))
  m2errs=np.zeros(len(Nlins))
  print('starting Beta='+str(Betas[i]))
  for j in range(len(m2vals)):
    print('\t Nlin='+str(Nlins[j]))
    pfile=open('param.dat','w')
    pfile.write('%d %f %d %d %ld %d %s\n' %(Nlins[j],Betas[i],Neql,Nmcs,Nbin,SEED,method))
    pfile.close()
    os.system('./wolff > log.log')
    data=np.loadtxt('data.out')
    m2s=data[:,3]
    #calculate mean and error of binned results
    m2vals[j]=np.mean(m2s)
    m2errs[j]=np.std(m2s)/(np.sqrt(len(Nlins)-1))
  label='Beta='+str(Betas[i])
  plt.errorbar(1.0/Nlins,m2vals,yerr=m2errs,label=label)
plt.legend(loc='upper right')
plt.xlabel('1/L')
plt.ylabel('<m^2>')
plt.title('<m^2> vs 1/L at different Temperatures (Betas)')
plt.show()
