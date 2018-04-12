import numpy as np
import matplotlib.pyplot as plt


xcol=0
ycol=1
data=np.loadtxt("data.out")
t = data[:,xcol]
theta = data[:,ycol]

x=np.arange(0,100,0.1)
s=1.0*np.cos(x)*np.exp(-0.05*x)+0.25
plt.plot(t,theta,label="Calculated")
plt.plot(x,s,label="Analytical")

plt.xlabel('time')
plt.ylabel(r'Omega')
plt.title('Euler Method vs Analytical Result')
plt.grid(True)
plt.savefig("test.pdf")
plt.show()
