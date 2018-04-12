import matplotlib.pyplot as plt
import numpy as np



d=np.loadtxt("data.out")


fig, (ax1,ax2)= plt.subplots(1,2)
ax1.plot(d)
ax1.set_xlabel('n')
ax1.set_ylabel('x')

ax2.hist(d,bins=20,histtype='step')
ax2.set_xlabel('x')
ax2.set_ylabel('P(x)')

plt.tight_layout()

plt.show()
