import numpy

t=numpy.arange(0.,2,0.1)

# some crazy function
f=numpy.sin(t)+6. + numpy.power(t,2)/20.

print ("f is",f)

# Fourier transform

ft = numpy.fft.fft(f)

print ("ft of f is",ft)

print ("ift of ft of f is", numpy.fft.ifft(ft))

# check the difference

print ("difference is", f-numpy.fft.ifft(ft))

