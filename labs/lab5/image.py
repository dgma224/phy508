import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread('einsetin.png')


mat=img[:,:,0]
xvals,yvals=mat.shape
print(mat.shape)
#fft the einstein thing
fftmat=np.fft.fft2(mat)
#now remove the middle portions
midx = int(xvals/2)
midy = int(yvals/2)
xpercent=99.5
ypercent=99.5
hdx=int(xpercent/200*xvals)
hdy=int(ypercent/200*yvals)
fftmat[midx-hdx:midx+hdx,midy-hdy:midy+hdy]=0.


fftmat=np.fft.ifft2(fftmat)

mati=np.absolute(fftmat)

edited=np.empty_like(img)
for i in range(3):
   edited[:,:,i]=mati

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(edited)
plt.show()
