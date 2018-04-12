import matplotlib.pyplot as plt
import numpy as np
import sys

if(len(sys.argv) < 2):
  print('Not enough inputs: python plot.py filetoplot')
  sys.exit() 

d=np.loadtxt(sys.argv[1])
plt.imshow(d,cmap='Greys',interpolation='nearest')
plt.show()
