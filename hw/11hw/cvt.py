import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time

Nlins=np.logspace(1,7,7,base=2)
Temps=np.logspace(0.1,1.5,20)
Nbs=100 #number of botstrap tests
Neql=1000
Nbin=1000
Nmcs=10
SEED=10
method='sqlatt_PBC'

def cvfunc(data,Ns,T):
  e=np.mean(data[:,0])
  e2=np.mean(data[:,1])
  return Ns/(T*T)*(e2-e*e)

for i in range(len(Nlins)):
  print('Nlin='+str(Nlins[i]))
  Ns=Nlins[i]*Nlins[i]
  cvvals=np.zeros(len(Temps))
  cverrs=np.zeros(len(Temps))
  #now run the code once for each temperature
  for j in range(len(Temps)):
    print('\tT='+str(Temps[j]))
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
      tempcv[k]=cvfunc(randdata,Ns,Temps[j])
    #use original data for mean
    cvvals[j]=cvfunc(data,Ns,Temps[j])
    cverrs[j]=np.std(tempcv)
  label='L='+str(Nlins[i])
  plt.errorbar(Temps,cvvals,yerr=cverrs,label=label)
plt.xscale('log')
plt.xlabel('Temperature (log scale)')
plt.ylabel('Specific Heat')
plt.show()

