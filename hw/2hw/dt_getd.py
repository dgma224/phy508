# runs pndlm program for increasing values of Nstep
#
import os
import numpy

gbl=1.; kappa=0.3; T_D=1.0; F_D=0;
ic_ang=0.1; ic_avel=0.0; t_final=10;
Nstep=2; method="runge_kutta";

for i in range(14):
	pfile= open('param.dat','w')
	pfile.write('%f %f %f %f\n' %(gbl,kappa,F_D,T_D))
	pfile.write('%f %f %f\n'%(ic_ang,ic_avel,t_final))
	pfile.write('%d %s\n'%(Nstep,method))
	pfile.close()

	os.system('./simple_pendulum > pndlm.log')

	data=numpy.loadtxt('data.out')

	print(Nstep, data[Nstep][1], data[Nstep][2], data[Nstep][3])
	Nstep*=2;
	
#end
