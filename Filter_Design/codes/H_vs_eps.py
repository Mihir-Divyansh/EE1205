import numpy as np
import matplotlib.pyplot as plt

eps = np.linspace(0.28, 0.61, 11)
def cheby_4(x): 
    return 8*x**4 + 8*x**2 + 1

def H_LP(w, epsilon): 
    H_mag = 1/(1+(epsilon**2)*(cheby_4(w))**2)**(0.5)
    return H_mag
omega = np.linspace(0, 2, 400)
for i in range(11):
    plt.plot(omega, abs(H_LP(1j*omega, eps[i])), label = '$\epsilon$ = %.2f' %(eps[i]))

plt.grid(True)
plt.legend()
plt.xlabel('$\Omega_L$')
plt.ylabel('$H_{LP}$')
# plt.savefig("../figs/HvE.png")
plt.savefig("HvE.png")