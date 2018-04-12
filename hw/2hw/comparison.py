#this code will plot the difference between the non-linear and the linear case
import numpy
import matplotlib.pyplot as plt
import os

gbl=1.; kappa=0.3; T_D=1.0; F_D=0;
ic_ang=0.1; ic_avel=0.0; t_final=10;
Nstep=16384; method="runge_kutta";
#do the two euler method codes and get data
method="euler"
pfile= open('param.dat','w')
pfile.write('%f %f %f %f\n' %(gbl,kappa,F_D,T_D))
pfile.write('%f %f %f\n'%(ic_ang,ic_avel,t_final))
pfile.write('%d %s\n'%(Nstep,method))
pfile.close()

os.system('./simple_pendulum > pndlm.log')
lineeuler=numpy.loadtxt('data.out')
os.system('./nl_pendulum > pndlm.log')
noneuler=numpy.loadtxt('data.out')

#do the two euler-cromer method codes

method="euler_cromer"
pfile= open('param.dat','w')
pfile.write('%f %f %f %f\n' %(gbl,kappa,F_D,T_D))
pfile.write('%f %f %f\n'%(ic_ang,ic_avel,t_final))
pfile.write('%d %s\n'%(Nstep,method))
pfile.close()

os.system('./simple_pendulum > pndlm.log')
linecromer=numpy.loadtxt('data.out')
os.system('./nl_pendulum > pndlm.log')
noncromer=numpy.loadtxt('data.out')

method="runge_kutta"
pfile= open('param.dat','w')
pfile.write('%f %f %f %f\n' %(gbl,kappa,F_D,T_D))
pfile.write('%f %f %f\n'%(ic_ang,ic_avel,t_final))
pfile.write('%d %s\n'%(Nstep,method))
pfile.close()

os.system('./simple_pendulum > pndlm.log')
linerunge=numpy.loadtxt('data.out')
os.system('./nl_pendulum > pndlm.log')
nonrunge=numpy.loadtxt('data.out')


#now all of the data sets have been loaded, create the comparison graphs
plt.plot(lineeuler[:,0],lineeuler[:,1],'red',label='linear')
plt.plot(noneuler[:,0],noneuler[:,1],'blue',label='nonlinear')
plt.legend(loc='upper right')
plt.xlabel('Time')
plt.ylabel('Angular Position')
plt.title('Euler Method Linear vs Non-linear 16384 Steps')
plt.grid(True)
plt.savefig("eulercompang16384.pdf")
plt.clf()


plt.plot(linecromer[:,0],linecromer[:,1],'red',label='linear')
plt.plot(noncromer[:,0],noncromer[:,1],'blue',label='nonlinear')
plt.legend(loc='upper right')
plt.xlabel('Time')
plt.ylabel('Angular Position')
plt.title('Euler-Cromer Method Linear vs Non-linear 16384 Steps')
plt.grid(True)
plt.savefig("cromercompang16384.pdf")
plt.clf()


plt.plot(linerunge[:,0],linerunge[:,1],'red',label='linear')
plt.plot(nonrunge[:,0],nonrunge[:,1],'blue',label='nonlinear')
plt.legend(loc='upper right')
plt.xlabel('Time')
plt.ylabel('Angular Position')
plt.title('Runge-Kutta Method Linear vs Non-linear 16384 Steps')
plt.grid(True)
plt.savefig("rungecompang16384.pdf")
plt.clf()
