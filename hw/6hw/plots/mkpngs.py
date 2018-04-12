import matplotlib.pyplot as plt
import numpy as np
import sys
import glob
import os
import time

os.chdir(".")
names=[]

for file in glob.glob("*.clust"):
  names.append(file)

print(len(names))

def f(i):
  return np.loadtxt(str(i)+'.clust')


test=f(0)
xdim,ydim=test.shape
fig,ax=plt.subplots()
plt.imshow(f(0),cmap='Greys',interpolation='nearest')
ax.autoscale(False)
ax.set_xlim(0,xdim)
ax.set_ylim(0,ydim)

#get x and y dimensions
print('Where to start?')
start = int(input())
tlast=time.time()
for i in range(start,len(names)):
  if i%10==0:
    print(str(i)+' : ' + str(time.time()-tlast))
    tlast=time.time()
  ax.imshow(f(i),cmap='Greys',interpolation='nearest')
  #fig.canvas.draw()#fig.show()
  fig.savefig('./pngs/'+str(i))
  #fig.canvas.flush_events()
  #ax.clear()
