import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sounddevice as sd
import time
from scipy.io import wavfile
from scipy.fftpack import fft
#samplerate1, audio1 = wavfile.read('audio1.wav')  # Fs : 44100 |  samples: 145530


#Audio 2
samplerate2, audio2 = wavfile.read('audio2.wav')  # Fs : 22050 |  samples: 55125  | t: 2.50s
T2 = 1/samplerate2; #time for one sample
window2 = 0.1; # 100ms
soundLength2 = 2.5;
samples_in_window2 = samplerate2 / 10; # 2205

for i in range(0,25):
    startingSample = i *samples_in_window2
    startingSample = int(startingSample)
    slicedData = audio2[startingSample:startingSample + int(samples_in_window2)]

    print(i,":  | samples : ",startingSample," - ", int(startingSample + samples_in_window2),"   |   ", i*100,"ms - ",(i+1) * 100,"ms")
    dft = fft(slicedData)

    #first and only plot
    if(i == 11):
        x_axis_for_sliced_data = np.arange(10*samples_in_window2 , 11*samples_in_window2) *T2
        #print(x_axis_for_sliced_data)

        plt.subplot(4, 2, 6)
        plt.xlim([1, 1.1])
        plt.plot( x_axis_for_sliced_data,slicedData)
        plt.title("D2_Signal ( 1000ms - 1100ms )")

        plt.subplot(4, 2, 8)
        plt.ylim(0,12)
        plt.xlim([1, 1.1])
        plt.plot(x_axis_for_sliced_data, np.abs(dft))
        plt.title("D2_DFT Magnitude ( 1000ms - 1100ms )")
        plt.show()

