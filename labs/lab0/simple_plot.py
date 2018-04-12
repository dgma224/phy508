
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('V(t)')
plt.grid(False)
plt.savefig("test.pdf")
plt.show()
