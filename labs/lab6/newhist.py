#this code finds the full width half max and does that plot

import matplotlib.pyplot as plt
import numpy as np
import os
import random
#do a loop for larger and larger numbers of observations
SEED = 10
numobs=2
numreps=1000
ns = 16
yvals = np.zeros(ns)
xvals = np.zeros(ns)
testvals = np.zeros(ns)
for i in range(ns):
  print('numobs = '+str(numobs))
  xvals[i] = numobs;
  os.system('./clt '+str(random.randrange(100))+' '+str(int(numobs)) + ' '+str(int(numreps))+' > log.log')
  data = np.loadtxt('data.out')
  yvals[i] = np.std(data)#relationship between FWHM and standard deviation
  numobs*=2
  #plt.hist(data,bins=20, histtype='step')
  #plt.show()
plt.loglog(xvals, yvals)
plt.xlabel("Number of Observations")
plt.ylabel("FWHM")
plt.title("FWHM versus Observations")
plt.grid(True)
plt.show()
