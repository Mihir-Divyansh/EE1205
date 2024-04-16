import soundfile as sf
import numpy as np
from scipy import signal
import scipy
# import librosa

#read .wav file 
input_signal,f_s = sf.read('My_Voice.wav') 

order=4 #Setting the order of the filter

f_c=4000.0  #cutoff frquency 

Wn=2*f_c/f_s   #digital frequency

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 
print(b)
print(a)
#filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a, input_signal[:,1], padlen=1)

#write the output signal into .wav file
sf.write('My_Voice_With_Reduced_Noise.wav', output_signal, f_s) 
