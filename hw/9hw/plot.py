#this python code will plot each of the four measurements for a range of temps
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import sys

#range of temperatures
temps=np.logspace(-2.0,3.0,20,base=10.0)

#input parameters for the monte carlo
Nlin=100
Neql=1000
Nmcs=100
Nbin=100
SEED=100
method='sqlatt_PBC'

#measurement arrays
eners=np.zeros(len(temps))
mags=np.zeros(len(temps))
eners2=np.zeros(len(temps))
mags2=np.zeros(len(temps))
errener=np.zeros(len(temps))
errmags=np.zeros(len(temps))
errener2=np.zeros(len(temps))
errmags2=np.zeros(len(temps))

for i in range(len(temps)):
  pfile=open('param.dat','w')
  pfile.write('%d %f %d %d %d %d %s\n' %(Nlin,1.0/(temps[i]),Neql,Nmcs,Nbin,SEED,method))
  pfile.close()
  print('t='+str(temps[i])+' starting')
  os.system('./ising > log.log')
  data=np.loadtxt('data.out')
  eners[i]=np.mean(data[:,0])
  eners2[i]=np.mean(data[:,1])
  mags[i]=np.mean(data[:,2])
  mags2[i]=np.mean(data[:,3])
  #calculate errors
  errener[i]=np.std(data[:,0])
  errener2[i]=np.std(data[:,1])
  errmags[i]=np.std(data[:,2])
  errmags2[i]=np.std(data[:,3])

plt.errorbar(temps,eners,xerr=0.0,yerr=errener)
plt.xscale("log",basex=10)
plt.xlabel('Temperature')
plt.ylabel('<e>')
plt.title('<e> as a function of Temperature')
plt.savefig('eners.png')

plt.clf()
plt.errorbar(temps,eners2,xerr=0.0,yerr=errener2)
plt.xscale("log",basex=10)
plt.xlabel('Temperature')
plt.ylabel('<e^2>')
plt.title('<e^2> as a function of Temperature')
plt.savefig('eners2.png')

plt.clf()
plt.errorbar(temps,mags,xerr=0.0,yerr=errmags)
plt.xscale("log",basex=10)
plt.xlabel('Temperature')
plt.ylabel('<m>')
plt.title('<m> as a function of Temperature')
plt.savefig('mags.png')

plt.clf()
plt.errorbar(temps,mags2,xerr=0.0,yerr=errmags2)
plt.xscale("log",basex=10)
plt.yscale("log",basey=10)
plt.xlabel('Temperature')
plt.ylabel('<m^2>')
plt.title('<m^2> as a function of Temperature')
plt.savefig('mags2.png')


