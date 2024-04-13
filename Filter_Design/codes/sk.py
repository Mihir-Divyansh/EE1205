import numpy as np
import matplotlib.pyplot as plt

N=4
eps = 0.29
def A (k):
    return (np.pi/(2*N))*(2*k+1)
B = np.arcsinh(1/eps)/N

s=[-(np.sin(A(i))*np.sinh(B)+1j*np.cos(A(i))*np.cosh(B)) for i in range(2*N)]

re_s_n = [s[i].real for i in range(N)]
im_s_n = [s[i].imag for i in range(N)] 
re_s_p = [s[i].real for i in range(N+1, 2*N)]
im_s_p = [s[i].imag for i in range(N+1, 2*N)] 

plt.scatter(re_s_n, im_s_n, color = 'red', label = "Left Side ")
plt.scatter(re_s_p, im_s_p, color = 'blue', label = "Right Side ")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.grid(True)
plt.legend()
plt.savefig("../figs/sk_pole_zero.plot")
# plt.savefig("sk_pole_zero.png")
