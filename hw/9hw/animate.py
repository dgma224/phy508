import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import glob,os
os.chdir(".")

spins=400
#figure
def f(i):
  return np.loadtxt('conf'+str(i)+'.spin')

fig=plt.figure()

ims = []
for i in range(spins):
  im = plt.imshow(f(i), cmap='Greys', interpolation='nearest',animated=True)
  ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
ani.save('test.gif')
plt.show()
