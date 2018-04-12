import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

if len(sys.argv) != 2:
  sys.exit("please input: filename")

data = np.loadtxt(sys.argv[1])
dt=data[:,0]
theta=data[:,1]

def func(x,a,b,c):
  return a+b*x**c
res,blah = curve_fit(func,dt,theta)
p=np.poly1d(np.polyfit(dt,theta,3))
xvals=np.linspace(dt[0],dt[-1],100)
plt.xlabel('dt')
plt.ylabel('theta')
plt.scatter(dt,theta,label='Data')
plt.plot(xvals,func(xvals,*res),label='PowFit')
plt.plot(xvals,p(xvals),label='Polyfit')
plt.legend(loc='upper left')
plt.show()
print(p(0))
print(func(0,*res))
