import numpy as np
import matplotlib.pyplot as plt

# Define the range of 'n'
n = np.arange(-1000, 1001)

# Calculate the values of impulse response
h_lp = np.where((n != 0) & (n >= -100) & (n <= 100), 2 * np.sin(n * np.pi / 40) * np.cos(n * 0.365 * np.pi) / (n * np.pi), 0)

# Compute the DFT of the impulse response
h_lp_fft = np.fft.fftshift(np.fft.fft(h_lp))

# Define the frequency axis according to normalised frequency
N = len(n)
freq = np.fft.fftshift(np.fft.fftfreq(N)) * 2 * np.pi

# Plot
plt.plot(freq / np.pi, np.abs(h_lp_fft))
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{bp}(\omega)|$')
plt.title("FIR BAND PASS FILTER")
plt.xlim(-0.7, 0.7)
plt.grid(True)
plt.savefig("FIR_Bandpass_Filter.png")