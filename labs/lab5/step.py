import numpy as np
import matplotlib.pyplot as plt


numdel=980
N=1000
x = np.arange(N)
fx = 0*x
fx[400:600]=1
fx[600:700]=2

ft=np.fft.fft(fx)
#now delete the middle range from the FFT
midval=N/2
ft[int(midval-numdel/2):int(midval+numdel/2)]=0.
ffti=np.fft.ifft(ft)
plt.plot(x,np.absolute(ffti), label='FFT Array')
plt.plot(x,fx, label='Original')
plt.legend(loc='upper right')
plt.show()
