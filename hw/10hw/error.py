import matplotlib.pyplot as plt
import numpy as np

#open analysis file and sort into arrays
data=np.loadtxt("data.out")
asizes=data[:,0]
xprobs=data[:,1]
yprobs=data[:,2]
tprobs=data[:,3]
nlin=16.0
b=0.1
asize=np.mean(asizes)
errasize=np.std(asizes)
xprob=np.mean(xprobs)
errxprob=np.std(xprobs)
yprob=np.mean(yprobs)
erryprob=np.std(yprobs)
tprob=np.mean(tprobs)*nlin*b
errtprob=np.std(tprobs)*nlin*b

print(str(asize)+' : '+str(errasize))
print(str(xprob)+' : '+str(errxprob))
print(str(yprob)+' : '+str(erryprob))
print(str(tprob)+' : '+str(errtprob))
