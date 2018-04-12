import numpy as np
import matplotlib.pyplot as plt


xcol=0
ycol=1
data=np.loadtxt("data.out")
t = data[:,xcol]
theta = data[:,ycol]

plt.plot(t,theta,label="Calculated")

plt.xlabel('time')
plt.ylabel(r'Omega')
plt.title('Euler Method')
plt.grid(True)
plt.savefig("eulerdefault.pdf")
plt.show()
