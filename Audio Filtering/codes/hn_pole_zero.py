import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf

input_signal, fs = sf.read('My_Voice.wav')

sampl_freq = fs

order = 4

cutoff_freq = 2000.0

Wn = 2 * cutoff_freq / sampl_freq  

b, a = signal.butter(order, Wn, 'low') 

zeroes, poles, gain = signal.tf2zpk(b,a)

plt.figure(figsize=(10, 8))
plt.scatter(zeroes.real, zeroes.imag, marker='o', color='b', label='Zeroes', s=100)
plt.scatter(poles.real, poles.imag, marker='x', color='r', label='Poles', s=100)
plt.axvline(0, color='k', linestyle='--', linewidth=0.5)
plt.axhline(0, color='k', linestyle='--', linewidth=0.5)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole-Zero Plot')
plt.legend()
plt.grid(True)
plt.savefig('../figs/Pole-Zero Plot')