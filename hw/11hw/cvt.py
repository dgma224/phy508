import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time

Nlins=[75]
Betas=np.flip(np.arange(0.25,0.7,0.01),0)
Temps=1/Betas
Nbs=100 #number of botstrap tests
Neql=1000
Nbin=10000
Nmcs=20
SEED=10
method='sqlatt_PBC'

def cvfunc(data,Ns,T):
  e=np.mean(data[:,0])
  e2=np.mean(data[:,1])
  return Ns/(T*T)*(e2-e*e)

for i in range(len(Nlins)):
  #print('Nlin='+str(Nlins[i]))
  Ns=Nlins[i]*Nlins[i]
  cvvals=np.zeros(len(Temps))
  cverrs=np.zeros(len(Temps))
  #now run the code once for each temperature
  for j in range(len(Temps)):
    #print('\tBeta='+str(Betas[j]))
    pfile=open('param.dat','w')
    pfile.write('%d %f %d %d %ld %d %s\n' %(Nlins[i],1.0/Temps[j],Neql,Nmcs,Nbin,SEED,method))
    pfile.close()
    os.system('./wolff > log.log')
    data=np.loadtxt('data.out')
    cvvals[j]=cvfunc(data,Ns,Temps[j])
    #now generate our random data sets and bootstrap
    tempcv=np.zeros(Nbs)
    for k in range(Nbs):
      randlocs=np.random.random_integers(0,Nbin-1,Nbin-1)
      randdata=data[randlocs]
      tempcv[k]=cvfunc(randdata,Ns,Temps[j])
    #use original data for mean
    cverrs[j]=np.std(tempcv)
    print(str(Nlins[i])+' '+str(Betas[j])+' '+str(cvvals[j])+' '+str(cverrs[j]))
  label='L='+str(Nlins[i])
  normalize=np.max(cvvals)
  cvvals=cvvals/normalize
  cverrs=cverrs/normalize
'''
  plt.errorbar(Betas,cvvals,yerr=cverrs,label=label)
plt.legend(loc='upper right')
plt.xlim(0.9,0.1)
plt.xlabel('Beta')
plt.ylabel('Specific Heat')
plt.show()
'''
