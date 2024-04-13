import numpy as np
import matplotlib.pyplot as plt 

s1 = -0.1907 - 1.0322j
s2 = -0.4604 - 0.4276j
s3 = -0.4604 + 0.4276j
s4 = -0.1907 + 1.0322j

den = np.poly([s1, s2, s3, s4])

w = np.linspace(0,2, 100)
s = 1j*w
num = 0.4166
H =num / np.polyval(den, s)
H_mag = np.abs(H)

eps = 0.3
def cheby_4(x): 
    return 8*x**4 + 8*x**2 + 1

def H_LP(w, epsilon): 
    H_mag = 1/(1+(epsilon**2)*(cheby_4(w))**2)**(0.5)
    return H_mag
plt.plot (w, H_mag, marker = 'o', label = 'Design')
plt.plot(w, abs(H_LP(1j*w, eps)), label = 'Simulation')
plt.grid(True)
plt.legend()
plt.xlabel('$\Omega_L$')
plt.ylabel('$H_{LP}$')
# plt.savefig("../figs/HvE.png")
plt.savefig("Design vs Simulation.png")