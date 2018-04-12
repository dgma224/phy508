#this code will run the logmap code many times with different starting values
import numpy as np
import matplotlib.pyplot as plt
import os
x0=0.5
n=100
xlow=0.890
xhigh=0.895
ylow=0.34
yhigh=0.36
r=np.arange(xlow, xhigh, 0.00001)
data=np.zeros((r.size,n+1),dtype=np.double)
xvals=np.zeros_like(data)
for i in range(r.size):
  xvals[i][:]=r[i]
#print(xvals)
for i in range(r.size):
  pfile = open('param.dat','w')
  pfile.write('%f %f %f\n' %(r[i],x0,n))
  pfile.close()
  os.system('./logmap')
  temp=np.loadtxt('data.out')
  data[i]=temp
  #print(data[i][40:])
  plt.scatter(xvals[i][90:],data[i][90:],marker='.')
plt.xlabel('r value')
plt.ylabel('Final X Value')
plt.xlim(xlow,xhigh)
plt.ylim(ylow,yhigh)
plt.show()
#now create the plot of the data
