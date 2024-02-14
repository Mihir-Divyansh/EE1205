#beautiful code btw: (sadly doesn't produce good graph)
#from sympy import plot_implicit, Eq
#from sympy.abc import x, y

#a = -4
#b = 2
#plot_implicit(Eq(y-a*x-b/x,0), (x, -10, 10), (y, -10, 10))

import numpy as np
import matplotlib.pyplot as plt

y=np.loadtxt("values.dat", delimiter=' ')

n1=range(0,100)
n2=range(100, 200)
# Generate x values
x_p_values = np.linspace(0.01, 5, 100)  
x_n_values = np.linspace(-5, -0.01, 100)
# Calculate y values
y_p_values = y[n2]
y_n_values = y[n1]



plt.plot(x_p_values, y_p_values, color='blue', label='$y = -4x - \\dfrac{2}{x}$')
plt.plot(x_n_values, y_n_values, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y(x)$')
plt.grid(True)
plt.legend()
plt.savefig("../figs/fig.png")