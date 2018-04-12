import numpy as np
import sys


Ndata=10

x =np.linspace(1,40,Ndata)
y = 3.5*x+10.0
err = 10.0*np.random.rand(Ndata) # create random error bars
y += err*np.random.randn(Ndata) # add noise to data according to error bars

for i in range(Ndata):
	print (x[i],y[i],err[i])
