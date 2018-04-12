#this is my code for the exact solution and for the resonance part
#it currently prints to terminal the data for the resonance part of the 
#assignment but can be easily modified to do the exact solution part
import numpy as np
import matplotlib.pyplot as plt
F_D=1.0
w=1.0
k=0.1
T_D=2.0*3.1415/2.0
x=np.arange(0,100,0.01)
td=np.arange(0.01,10,0.01)

T_D=2.0*3.1415/td
#exact_solution=F_D/np.sqrt((w*w-T_D*T_D)**2.0+k**2.0*T_D**2.0)*np.sin((T_D-np.arctan(-k*T_D/(w**2.0-T_D**2.0)))*x)

resonance=F_D/np.sqrt((w*w-T_D*T_D)**2.0+k**2.0*T_D**2.0)
for i in range(0,np.size(td)):
	print(td[i],resonance[i])

