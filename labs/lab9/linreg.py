import numpy as np
import sys
import matplotlib.pyplot as plt

if len(sys.argv) != 6:
        sys.exit("please input: filename, x, y, dy, fit_type (lin/pow/exp) \n")

data=np.loadtxt(sys.argv[1])
xdata=data[:,int(sys.argv[2])]
ydata=data[:,int(sys.argv[3])]
Ndata = np.size(xdata)
if int(sys.argv[4])>=0:
	dydata=data[:,int(sys.argv[4])];
else:
	dydata=np.ones(Ndata);

if (sys.argv[5] == "lin"):
	print ("lin: y = a+bx")
	dy=dydata
	y=ydata
	x=xdata
elif (sys.argv[5] == "pow"):
	print ("pow: y = ax^b")
	dy = dydata/ydata
	y = np.log(ydata)
	x = np.log(xdata)	
elif (sys.argv[5] == "exp"):
	print("exp: y = ae^{xb}")
	dy = dydata/ydata
	y = np.log(ydata)	
	x=xdata
else:
	print("dont recognize fit_type, exiting")
	sys.exit(1)


S=np.sum(1./(dy*dy))
Sx=np.sum(x/(dy*dy))
Sy=np.sum(y/(dy*dy))
Sxx=np.sum((x*x)/(dy*dy))
Sxy=np.sum((x*y)/(dy*dy))
Delta = S*Sxx-Sx*Sx
a=(Sxx*Sy-Sx*Sxy)/Delta
b=(S*Sxy-Sx*Sy)/Delta
siga = np.sqrt(Sxx/Delta)
sigb = np.sqrt(S/Delta)
yc=a+b*x
chisqpd= np.sum(((y-yc)/dy)**2)/float(Ndata-2)

plt.errorbar(xdata,ydata,dydata,fmt='o',capsize=5,label="data")
	 
print("Number of data points = ",Ndata)
if sys.argv[5] == "lin":
	print("a = ",a,siga)
	print("b = ", b, sigb)
	fitx=np.array([np.min(xdata),np.max(xdata)])
	fity= a+ b*fitx

if sys.argv[5] == "pow":
	print("a = ",np.exp(a),np.exp(a)*siga)
	print("b = ", b, sigb)
	fitx=np.array([np.min(xdata),np.max(xdata)])
	fity= np.exp(a)*(fitx**b)
	plt.xscale('log')
	plt.yscale('log')
if sys.argv[5] == "exp":
	print("a = ",np.exp(a),np.exp(a)*siga)
	print("b = ", b, sigb)
	fitx=np.array([np.min(xdata),np.max(xdata)])
	fity= np.exp(a)*np.exp(fitx*b)
	plt.yscale('log')

print("Chisq/(N-2) = ",chisqpd)

plt.plot(fitx,fity,'--',label="fit")
plt.legend()
plt.show()
