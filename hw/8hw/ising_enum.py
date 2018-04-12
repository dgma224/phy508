import numpy as np
import sys
import matplotlib.pyplot as plt

Ls=[3]

Tmin=-2
Tmax=10
numT=20
temps=np.logspace(Tmin,Tmax,num=numT,base=2.0)
temps[:]=1.0/0.25
#calculate magnetism
def get_mag(spin):
  return np.sum(spin)

#calculate energies
def get_ener(spin):
  L=int(np.sqrt(len(spin)))
  spm=np.reshape(spin,(L,L))#create LxL matrix
  spx=np.roll(spm,1,axis=1)
  spy=np.roll(spm,1,axis=0)
  enerx=np.dot(spin,spx.flatten())
  enery=np.dot(spin,spy.flatten())
  return -1*(enerx+enery)

#get array of energies and magnetizations for each state
def enermags(Nstate,Nsite,L):
  mags=np.zeros(Nstate)
  eners=np.zeros(Nstate)
  for state in range(Nstate):
    svec=np.array(list(np.binary_repr(state).zfill(Nsite))).astype(np.int8)
    spin=2*svec-1
    mags[state]=float(get_mag(spin))
    eners[state]=get_ener(spin)
  return eners,mags
  
#now calculate energies and magnetizations for a range of temperatures
numNsite=len(Ls)
expecteners=np.ndarray(shape=(numNsite,len(temps)))
expecteners2=np.empty_like(expecteners)
expectmags=np.empty_like(expecteners)
expectmags2=np.empty_like(expecteners)
specval=np.empty_like(expecteners)
susceptval=np.empty_like(expecteners)
expectE=np.empty_like(expecteners)


for j in range(len(Ls)):
  Nsite=Ls[j]*Ls[j]
  Nstate=int(pow(2,Nsite))
  eners,mags=enermags(Nstate,Nsite,Ls[j])
  for i in range(len(temps)):
    T=temps[i]
    #normalization values
    normal=np.sum(np.exp(-1.0/float(T)*eners))
    topener=np.sum(eners/float(Nsite)*np.exp(-1.0/float(T)*eners))
    topmag=np.sum(mags/float(Nsite)*np.exp(-1.0/float(T)*eners))
    topener2=np.sum(eners*eners/float(Nsite)/float(Nsite)*np.exp(-1.0/float(T)*eners))
    topmag2=np.sum(mags*mags/float(Nsite)/float(Nsite)*np.exp(-1.0/float(T)*eners))
    topE=np.sum(eners*np.exp(-1.0/float(T)*eners))
    expecteners[j][i]=topener/normal
    expecteners2[j][i]=topener2/normal
    expectmags[j][i]=topmag/normal
    expectmags2[j][i]=topmag2/normal
    specval[j][i]=float(Nsite)/(float(T))*(expecteners2[j][i]-expecteners[j][i]**2.0)
    susceptval[j][i]=float(Nsite)/(float(T))*(expectmags2[j][i]-expectmags[j][i]**2.0)
    expectE[j][i]=topE/normal
print(expecteners)
print(susceptval)
'''
#creating the plots now
for i in range(numNsite):
  plt.semilogx(temps,expecteners[i],label='Nsites='+str(Ls[i]*Ls[i]))
plt.legend(loc='upper right')
plt.title('<e> vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('<e>')
plt.show()

for i in range(numNsite):
  plt.semilogx(temps,expecteners2[i],label='Nsites='+str(Ls[i]*Ls[i]))
plt.legend(loc='upper right')
plt.title('<e^2> vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('<e^2>')
plt.show()

for i in range(numNsite):
  plt.loglog(temps,expectmags[i],label='Nsites='+str(Ls[i]*Ls[i]))
plt.legend(loc='upper right')
plt.title('<m> vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('<m>')
plt.show()

for i in range(numNsite):
  plt.loglog(temps,expectmags2[i],label='Nsites='+str(Ls[i]*Ls[i]))
plt.legend(loc='upper right')
plt.title('<m^2> vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('<m^2>')
plt.show()

for i in range(numNsite):
  plt.loglog(temps,specval[i],label='Nsites='+str(Ls[i]*Ls[i]))
plt.legend(loc='upper right')
plt.title('Specific Heat vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('Specific Heat')
plt.show()

for i in range(numNsite):
  plt.loglog(temps,susceptval[i],label='Nsites='+str(Ls[i]*Ls[i]))
plt.legend(loc='upper right')
plt.title('Susceptability vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('Susceptability')
plt.show()

for i in range(numNsite):
  plt.semilogx(temps,expectE[i],label='Nsites='+str(Ls[i]*Ls[i]))
plt.legend(loc='upper right')
plt.title('Energy vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('Energy')
plt.show()
'''
