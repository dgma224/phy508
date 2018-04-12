
import numpy as np
import sys    

L=4
Nsite=L*L

# this is a simple program to learn som array maniuplations in numpy
# using these functions is much faster and neater than nested for loops
# this program gives you everything you need to compute Ising energy


print ("state: original state vector")
state = np.arange(Nsite)
print (state,"\n")

print("sp: converts it into a 4x4 matrix")
sp=np.reshape(state,(L,L))
print (sp,"\n")

print("spx: shifts sp by one unit in the x-axis with PBC")
spx=np.roll(sp,1,axis=1)
print (spx,"\n")

print("spy: shifts sp by one unit in y with PBC")
spy=np.roll(sp,1,axis=0)
print (spy,"\n")

print("flatten(): flattens spx matrix back into an array")
print (spx.flatten(),"\n")

print("dot(): computes nearest neighbor sum for x-bonds")
print (np.dot(state,spx.flatten()),"\n")


