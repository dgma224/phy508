import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time

Nlins=[16,64,128]
Betas=np.flip(np.arange(0.1,0.9,0.025),0)
Temps=1/Betas
Nbs=100 #number of botstrap tests
Neql=1000
Nbin=1000
Nmcs=10
SEED=10
method='sqlatt_PBC'

def brfunc(data):
  m4=np.mean(data[:,4])
  m2=np.mean(data[:,3])
  return m4/(m2*m2)

for i in range(len(Nlins)):
  print('Nlin='+str(Nlins[i]))
  Ns=Nlins[i]*Nlins[i]
  cvvals=np.zeros(len(Temps))
  cverrs=np.zeros(len(Temps))
  #now run the code once for each temperature
  for j in range(len(Temps)):
    print('\tBeta='+str(1/Temps[j]))
    pfile=open('param.dat','w')
    pfile.write('%d %f %d %d %ld %d %s\n' %(Nlins[i],1.0/Temps[j],Neql,Nmcs,Nbin,SEED,method))
    pfile.close()
    os.system('./wolff > log.log')
    data=np.loadtxt('data.out')
    #now generate our random data sets and bootstrap
    tempcv=np.zeros(Nbs)
    for k in range(Nbs):
      randlocs=np.random.random_integers(0,Nbin-1,Nbin-1)
      randdata=data[randlocs]
      tempcv[k]=brfunc(randdata)
    #use original data for mean
    cvvals[j]=brfunc(data)
    cverrs[j]=np.std(tempcv)
  label='L='+str(Nlins[i])
  plt.errorbar(Betas,cvvals,yerr=cverrs,label=label)
#plt.xscale('log')
plt.xlim(0.9,0.1)
plt.xlabel('Beta Value (1/T)')
plt.ylabel('Binder Ratio')
plt.legend(loc='upper right')
plt.show()

