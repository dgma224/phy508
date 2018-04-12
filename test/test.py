import numpy as np


a = np.arange(0,10,1)
b = np.fft.fft(a)

a2 = np.sum(a*np.conj(a))
b2 = np.sum(b*np.conj(b))

print(a2, b2)
