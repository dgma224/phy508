import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time

#initial parameters
Nlin=10
Ns=Nlin*Nlin
Beta=0.44
T=1/Beta 
Nbs=100 #number of bootstrap tests
#first load in the original data set
data=np.loadtxt('data.out')
numrow=len(data[:,0])
'''col0=energ,1=ener^2,2=mag,3=mag^2,4=mag^4'''

def brfunc(data):
  #first calculate m^4 average
  m4=np.mean(data[:,4])
  m2=np.mean(data[:,3])
  return m4/(m2*m2)

def cvfunc(data,Ns,T):
  e=np.mean(data[:,0])
  e2=np.mean(data[:,1])
  return Ns/(T*T)*(e2-e*e)

#create arrays for results
cvvals=np.zeros(Nbs)
brvals=np.zeros(Nbs)
for i in range (Nbs):
  #generate random row values
  randlocs=np.random.random_integers(0,numrow-1,numrow-1)
  randdata=data[randlocs]
  #calculate br and cv with this new array
  brvals[i]=brfunc(randdata)
  cvvals[i]=cvfunc(randdata,Ns,T)

#calculate average and standard deviation from these 
brave=np.mean(brvals)
cvave=np.mean(cvvals)
brstd=np.std(brvals)
cvstd=np.std(cvvals)
print('br= '+str(brave)+'+-'+str(brstd))
print('cv= '+str(cvave)+'+-'+str(cvstd))
