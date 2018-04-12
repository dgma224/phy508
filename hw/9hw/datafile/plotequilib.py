import matplotlib.pyplot as plt
import numpy as np

#load data files
xlen=50
ycol=0
data1=np.loadtxt('l100b001.out')
data2=np.loadtxt('l100b025.out')
data3=np.loadtxt('l100b05.out')
data4=np.loadtxt('l100b1.out')

xvals=np.arange(xlen)

plt.plot(xvals,data1[:xlen,ycol],label='B=0.01')
plt.plot(xvals,data2[:xlen,ycol],label='B=0.25')
plt.plot(xvals,data3[:xlen,ycol],label='B=0.5')
plt.plot(xvals,data4[:xlen,ycol],label='B=1')

plt.xlabel('Sweep Number')
plt.ylabel('<e>')
plt.title('<e> During Equillibriation, L=100')
plt.legend(loc='upper right')
plt.show()
