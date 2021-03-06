#this script will calculate the autocorrelation times
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time
from scipy.optimize import curve_fit
code='wolff'
#params
Nlins=[5,10,25,50,100]
beta=np.log(1+np.sqrt(2))/2
Neql=1000
Nmcs=1
Nbin=100000
SEED=100
latt='sqlatt_PBC'
corrtime=100

def func(x,a,b):
  return a*np.exp(-1.0*x/b)

for j in range(len(Nlins)):
  #now call the code to get the data
  #first call the code and get the data values
  print('Running '+str(code) +' with L='+str(Nlins[j]))
  pfile=open('param.dat','w')
  pfile.write('%d %f %d %d %ld %d %s\n' %(Nlins[j],beta,Neql,Nmcs,Nbin,SEED,latt))
  pfile.close()
  os.system('./'+str(code)+' > log.log')
  data=np.loadtxt('data.out')
  print('Analyzing '+str(Nlins[j]))
  #now need to call the code with a huge number of runs
  a=np.zeros(corrtime)
  mags=data[:,3]
  Asquared=np.mean(mags)**2 #average squared
  AA=np.mean(mags*mags)#average of the squared
  corrtimes=np.arange(corrtime)
  for i in range(corrtime):
    #create rolled array
    magst=np.roll(mags,-1*i) #roll the array backwards that many time units
    magst[Nbin-i:]=0
    AB=np.dot(magst,mags)/(float(Nbin-i))#average of the two multiplied together
    a[i]=(AB-Asquared)/(AA-Asquared)
  legend='L'+str(Nlins[j])
  plt.plot(corrtimes,a,label=legend)
  #now do the curve fitting
  res,blah=curve_fit(func,corrtimes,a)
  print('L='+str(Nlins[j])+' : a='+str(res[0])+', b='+str(res[1]))
  #now do integrated time thingy
  print('Theta = '+str(np.sum(a)))
plt.legend(loc='upper right')
plt.title(str(code)+' Algorithm Correlation: B='+str(beta))
plt.xlabel('Time (number of sweeps)')
plt.ylabel('Correlation Coefficient')
plt.show()
