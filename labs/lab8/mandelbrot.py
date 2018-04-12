import numpy as np

nmax=20 #number of zn to calculate in series
maxval=5 #maximum allowed value
#defining ranges of real and imaginary parts of c
xmin=-2
xmax=2
ymin=-2
ymax=2
xnum=10000
ynum=10000
xinter=float(xmax-xmin)/(float(xnum))
yinter=float(ymax-ymin)/(float(ynum))
xvals=np.arange(xmin,xmax,xinter)
yvals=np.arange(ymin,ymax,yinter)*1j
#creating matrix of c values
xx,yy=np.meshgrid(xvals,yvals)

#function that returns c values
def zn(cx,cy,n,maxval):
  zlast=cx+cy
  i = 0
  while abs(zlast)<maxval and i < n:
    zlast=zlast*zlast+cx+cy
    i+=1
  if i==n:
    return -1
  else:
    return i-1
#making that function work on matrices
vfunc=np.vectorize(zn)
#results matrix
vals=np.empty([xnum,ynum],np.int16)
#executing function
vals[:,:]=vfunc(xx,yy,nmax,maxval)
#saving results
np.save("test",vals)
