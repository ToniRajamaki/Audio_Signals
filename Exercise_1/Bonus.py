# Bonus problem: (0.5 point)
# In problem1 downsample the sum of sinusoids x(t) by a factor of 2 using
# scipy.signal.resample. Write the downsampled signal into wav file. Plot the magnitude
# DFT and compare it with DFT of x(t). Explain and report your observation.

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sounddevice as sd
import time
from scipy.io import wavfile
from scipy.fftpack import fft
from scipy.signal import resample

def sinFunction(omega):


    return np.sin(omega*t_seq);

# y = A * sin(omegta * t + x )   =   Amplitude * sin( 2* pi *ft + x )

freqs = [100,500,1500,2500]

sampling_rate = 8000;
T = 1/sampling_rate;  # time it takes for 1 sample
t = 3 # the length we want for the signal
N = sampling_rate * t; # number of samples for given duration (t)

freq1 = 100
freq2 = 500
freq3 = 1500
freq4 = 2500

omega1 = 2*np.pi*freq1
omega2 = 2*np.pi*freq2
omega3 = 2*np.pi*freq3
omega4 = 2*np.pi*freq4

t_seq = np.arange(N) * T  #time stamps for each sample


y1 = sinFunction(omega1)
y2 = sinFunction(omega2)
y3 = sinFunction(omega3)
y4 = sinFunction(omega4)

x = np.arange(512) #  x_points

sum_y = y1+y2+y3+y4
downsampled_sum_y = resample(sum_y,12000)





plt.subplot(2,1,1)
dft_sum_signal = fft(downsampled_sum_y)
first_512_samples = downsampled_sum_y[0:512]
plt.plot(x,np.abs(first_512_samples))
plt.title(" Downsampled magnitude")




plt.subplot(2,1,2)
dft_sum_signal = fft(sum_y,512)
plt.plot(x, np.abs(dft_sum_signal))
plt.title("original Magnitude")



wavfile.write('downsampled_sumWav.wav',4000,downsampled_sum_y)


plt.show()

# Bonus problem
# I managed to downsample the sum signal, i took first 512 samples from the both of them and plotted their magnitudes.
# the downsampled one seems to be much more denser and there is no phase in the middle. Also when i tried to listen to the
# wav files, I noticed that the original one is higher.