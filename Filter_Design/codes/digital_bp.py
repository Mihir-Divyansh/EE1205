import numpy as np
import matplotlib.pyplot as plt 

s1 = -0.1907 - 1.0322j
s2 = -0.4604 - 0.4276j
s3 = -0.4604 + 0.4276j
s4 = -0.1907 + 1.0322j
G_LP = 0.4166
num = G_LP

s = [(-0.19070540764996763-1.0322426306409171j), (-0.46040358156644157-0.42756889727114933j), (-0.46040358156644157+0.4275688972711492j), (-0.19070540764996768+1.0322426306409171j)]
Omega_p1 = 0.5913
Omega_p2 = 0.702

Omega_s1 = 0.5662
Omega_s2 = 0.7361


B = 0.1107
Omega0 = 0.644
den = np.poly(2*s)

w = np.linspace(-2,2, 1000)
s1 = 1j*w
num = 0.4166
H =num / np.polyval(den, s1)
H_mag = np.abs(H)

eps = 0.3
def cheby_4(x): 
    return 8*x**4 + 8*x**2 + 1

def H_LP(z, epsilon): 
    
    s = (1-z**(-1))/(1+z**(-1))
    s_b = (s**2 + Omega0**2)/(B*s)
    w = s_b/1j
    
    H_mag = 1/(1+(epsilon**2)*(cheby_4(w))**2)**(0.5)
    return H_mag

# plt.plot (w, H_mag, marker = 'o', color = 'r', label = 'Design')
plt.plot(w/np.pi, abs(H_LP(np.exp(1j*w), eps)), color = 'orange')
plt.grid(True)
plt.title("Magnitude response of the Digital Band Pass Filter")
plt.xlabel('$\Omega_L$')
plt.ylabel('$H_{LP}$')

plt.savefig("Digital_BP.png")
plt.show()