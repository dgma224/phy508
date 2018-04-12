import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import glob,os
os.chdir(".")
names=[]

rep=50

#figure out how many files there are
for file in glob.glob("*.clust"):
  names.append(file)
print(len(names))
fig = plt.figure()

def f(i):
  return np.loadtxt(str(i)+'.clust')


ims = []
for i in range(len(names)):
  im = plt.imshow(f(i), cmap='Greys', interpolation='nearest',animated=True)
  ims.append([im])
for i in range(rep):
  im = plt.imshow(f(len(names)-1), cmap='Greys', interpolation='nearest', animated=True)
  ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
ani.save('test.gif')
plt.show()
