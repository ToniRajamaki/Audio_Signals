# Problem 1: Create a synthetic signal as a sum of sinusoids. (1 point)

# a) Create 4 sinusoids of 3 s length, with different amplitude, frequencies 100, 500, 1500,
# 2500 Hz, different phases, sampled at 8kHz. (Hint: how many samples the signal must
# have for 3 s length? take into account fs).
# b) Play and plot the sinusoids
# c) Add them up to x(t). Plot and play x(t). Write the signal to a wav file.
# d) Apply DFT (you can use scipy.fftpack.fft function. Select the number of DFT points,
# e.g., to 512)). Plot magnitude DFT.
# e ) Observe the components and relationship between nfft and frequency in Hz. (DFT has
# imaginary values x+iy, where x is amplitude information and y is phase). Report your
# observation.

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sounddevice as sd
import time

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

if(True):

    fig = plt.figure()


    plt.subplot(5,1,1)
    plt.ylim([-1.5, 1.5])
    plt.xlim([0, 0.02])
    plt.plot(t_seq,y1)
    plt.ylabel("100Hz")


    plt.subplot(5, 1, 2)
    plt.ylim([-1.5, 1.5])
    plt.xlim([0,0.02])
    plt.plot(t_seq,y2)
    plt.ylabel("500Hz")


    plt.subplot(5, 1, 3)
    plt.ylim([-1.5, 1.5])
    plt.xlim([0,0.02])
    plt.plot(t_seq,y3)
    plt.ylabel("1500Hz")


    plt.subplot(5, 1, 4)
    plt.ylim([-1.5, 1.5])
    plt.xlim([0,0.02])
    plt.plot(t_seq,y4)
    plt.ylabel("2500Hz")

    sum_y = y1+y2+y3+y4

    plt.subplot(5, 1, 5)
    plt.ylim([-5, 5])
    plt.xlim([0, 0.02])
    plt.plot(t_seq, sum_y)
    plt.ylabel("sum signal")
    plt.show()

    play = False
    if(play):
        sd.play(y1)
        time.sleep(2)
        sd.play(y2)
        time.sleep(2)
        sd.play(y3)
        time.sleep(2)
        sd.play(y4)
        time.sleep(2)
        sd.play(sum_y)



