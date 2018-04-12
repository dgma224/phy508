import numpy as np
import matplotlib.pyplot as plt

start=0.0
stop=50.0
step=0.05
numsteps=(stop-start)/step
x = np.arange(start, stop, step)

fx =np.sin(x)+np.cos(x/2.0+3.0)
fig, (ax1, ax2) = plt.subplots(1,2)

ax1.plot(x,fx)
ax1.set_ylabel('f(x)')
ax1.set_xlabel('x')

ft=np.fft.fft(fx)/numsteps

modft=np.roll(ft,int(numsteps/2.0))
xvals=np.arange(-1.0*numsteps/2.0, numsteps/2.0, 1.0)

ax2.plot(xvals,np.absolute(modft))
#ax2.set_yscale('log')

ax2.set_ylabel('FT of f(x)')
ax2.set_xlabel('Rolled over Index')
ax2.set_xlim(-100, 100)
plt.tight_layout()
plt.show()


