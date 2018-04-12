import numpy as np
import matplotlib.pyplot as plt
#actual values
exaang=-0.021482155
exavel=0.010061259

euler=np.loadtxt("euler.out")
crome=np.loadtxt("runge.dat")
#define variables
x=euler[:,0]
eulang=euler[:,1]
croang=crome[:,1]
eulvel=euler[:,2]
crovel=crome[:,2]

#do the first comparison to actual value plots
#create the filler arrays

angarray=np.full(14,exaang)
velarray=np.full(14,exavel)

#final angle for euler plot
plt.semilogx(x,eulang,'red',label='euler')
plt.semilogx(x,angarray,'blue',label='exact')
plt.legend(loc='upper right')
plt.xlabel('Nstep')
plt.ylabel('Final Angle')
plt.title('Euler Method Final Angle')
plt.grid(True)
plt.savefig("finangeulerplt.pdf")
plt.clf()

#final angle for euler-cromer plot
plt.semilogx(x,croang,'red',label='euler-cromer')
plt.semilogx(x,angarray,'blue',label='exact')
plt.legend(loc='upper right')
plt.xlabel('Nstep')
plt.ylabel('Final Angle')
plt.title('Euler-Cromer Method Final Angle')
plt.grid(True)
plt.savefig("finangcromerplt.pdf")
plt.clf()

#final angular velocity for euler plot
plt.semilogx(x,eulvel,'red',label='euler')
plt.semilogx(x,velarray,'blue',label='exact')
plt.legend(loc='upper right')
plt.xlabel('Nstep')
plt.ylabel('Final Angular Velocity')
plt.title('Euler Method Final Angle')
plt.grid(True)
plt.savefig("finveleulerplt.pdf")
plt.clf()

#final angular velocity for euler-cromer plot
plt.semilogx(x,crovel,'red',label='euler-cromer')
plt.semilogx(x,velarray,'blue',label='exact')
plt.legend(loc='upper right')
plt.xlabel('Nstep')
plt.ylabel('Final Angular Velocity')
plt.title('Euler-Cromer Method Final Angle')
plt.grid(True)
plt.savefig("finvelcromerplt.pdf")
plt.clf()

#subtract from the actual value
eulang=np.abs(eulang-exaang)
croang=np.abs(croang-exaang)
eulvel=np.abs(eulvel-exavel)
crovel=np.abs(crovel-exavel)

plt.loglog(x,eulang,'red',label='euler')
plt.loglog(x,croang,'blue',label='runge-kutta')
plt.legend(loc='upper right')
plt.xlabel('Nstep')
plt.ylabel('Error')
plt.title('Error vs Nstep for Angular Position')
plt.yticks(np.logspace(-9,1,11))
plt.grid(True)
plt.savefig("angplt.pdf")
plt.clf()


plt.loglog(x,eulvel,'red',label='euler')
plt.loglog(x,crovel,'blue',label='euler-cromer')
plt.legend(loc='upper right')
plt.xlabel('Nstep')
plt.ylabel('Error')
plt.title('Error vs Nstep for Angular Velocity')
plt.grid(True)
plt.savefig("velplt.pdf")
plt.clf()
