import numpy as np
import matplotlib.pyplot as plt

y=np.loadtxt("data.dat", delimiter='\t')
t=np.linspace(-5,5,10000)
s=np.linspace(-10,10,10000)
#Assigning columns to the different functions
x=y[:,0]
y_1=y[:,1]
H=y[:,2]
#Plotting input
plt.plot(t,x,color='blue', label="x(t)")
plt.title("Graph of Input")
plt.legend()
plt.grid(True)
plt.savefig('../figs/input.png')
#Plotting output
plt.clf()
plt.plot(t,y_1,color='red', label='$y(t)$')
plt.title("Graph of Output ")
plt.legend()
plt.grid(True)
plt.savefig('../figs/output.png')
#Plotting Transfer Function
plt.clf() #<-- Clears field of plot. Creates new file for plot
plt.plot(s,H,color='orange', label="$H(s)$")
plt.title("Transfer function of the system")
plt.legend()
plt.grid(True)
plt.savefig('../figs/transfer.png')


