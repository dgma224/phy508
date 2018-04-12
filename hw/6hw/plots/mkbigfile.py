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
i = 0
with open('onelargefile.txt','w') as outfile:
  for fname in names:
    if i % 10 == 0:
      print(i)
    with open(fname) as infile:
      for line in infile: 
        outfile.write(line)

    outfile.write('\n')
    i+=1
