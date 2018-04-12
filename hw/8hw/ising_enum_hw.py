import numpy as np
import sys    

L=2
Nsite = L*L
Nstate=int(pow(2,Nsite))
def get_mag(spin):    
    return np.sum(spin)

def get_ener(spin):    
    L=int(np.sqrt(len(spin)))
    spm=np.reshape(spin,(L,L))#create LxL matrix
    spx=np.roll(spm,1,axis=1)
    spy=np.roll(spm,1,axis=0)
    enerx=np.dot(spin,spx.flatten())
    enery=np.dot(spin,spy.flatten())
    return -1*(enerx+enery)


for state in range(Nstate):
    svec=np.array(list(np.binary_repr(state).zfill(Nsite))).astype(np.int8)
    spin=2*svec-1
    mag=get_mag(spin)
    ener=get_ener(spin)
    print ('STATE = ',state)
    print (np.reshape(spin,(L,L)))
    print ('M = ',mag,'; E = ',ener)
    print ()

