import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf



#sampling frequency obtained from the audio file
sampl_freq=44100 
T = 1.0/sampl_freq
#order of the filter
order=4

#cutoff frquency 4kHz
cutoff_freq=4000.0 

#digital frequency
Wn=2*cutoff_freq/sampl_freq  


# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

#DTFT
def H(s):
	num = np.polyval(b,((1+s*(T/2))/(1-s*(T/2)))**(-1))
	den = np.polyval(a,((1+s*(T/2))/(1-s*(T/2)))**(-1))
	H = num/den
	return H
		
#Input and Output
f = np.arange(0,5000,100)

#subplots
plt.plot(f, abs(H(1j*f)))
plt.xlabel('$f$')
plt.ylabel('$|H(f)| $')
plt.title("Frequency response of Filter")
plt.grid()
plt.savefig("../figs/Analog_Filter_Response.png")
