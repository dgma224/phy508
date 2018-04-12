import matplotlib.pyplot as plt
import numpy as np
import sys

if(len(sys.argv) < 2):
  print('Not enough inputs: python plot.py filetoplot')
  sys.exit() 


d=np.loadtxt(sys.argv[1])
cmap=plt.get_cmap('cool')
cmap.set_under('black')
plt.imshow(d,vmin=-0.5,cmap=cmap,interpolation='nearest')
plt.show()
