# Problem 2: Read an audio and observe the spectrum. (1 point)
# a) Read one of the provided audio files, play and plot the entire signal.
# b) Plot signal between 0.5 and 1 s.
# Do the following(c and d) in a loop (make it a function):
# c) Read the next 100 ms of the signal. (Hint: take into account fs; even better, make this
# frame length a parameter so you can always change it to a different value). Plot the signal.
# d) Apply DFT to this segment and plot the magnitude DFT.
# So the loop basically computes magnitude DFT for each of the 100 ms segments of the
# audio. You do not have to plot all the segments, only plotting the first segment and
# corresponding magnitude DFT is enough.


import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sounddevice as sd
import time
from scipy.io import wavfile
from scipy.fftpack import fft


samplerate, data2 = wavfile.read('audio2.wav')


# A.) and B.)
T = 1/samplerate; #time for one sample
total_samples = len(data2)
timeAxis = np.arange(total_samples) * T
plt.xlim([0.5, 1])
# plt.plot(timeAxis,data2)
# plt.show()
# sd.play(data)


# C.) and  D.)


window = 0.1; # 100ms
soundLength = 2.5;
samples_in_window = samplerate / 10; # 2205
data2_CD = data2[22050: int(11*samples_in_window)]


for i in range(11,25):
    startingSample = i *samples_in_window
    startingSample = int(startingSample)
    slicedData = data2[startingSample:startingSample + int(samples_in_window)]
    print(i," : " ,len(slicedData)," , samples : ",startingSample," - ", int(startingSample + samples_in_window), i*100,"ms - ",(i+1) * 100,"ms")

    #first and only plot
    if(i == 11):
        plt.plot(slicedData)
        plt.show()
