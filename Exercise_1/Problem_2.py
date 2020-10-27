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


samplerate2, data2 = wavfile.read('audio2.wav')
samplerate1, data1 = wavfile.read('audio1.wav')
print(samplerate1,"   ", len(data1))


# A.) and B.)
# Audio 2
T2 = 1/samplerate2; #time for one sample
total_samples2 = len(data2)
timeAxis2 = np.arange(total_samples2) * T2



# Audio1
T1 = 1/samplerate1; #time for one sample
total_samples1 = len(data1)
timeAxis1 = np.arange(total_samples1) * T1


plt.subplot(4,2,1)
plt.plot(data1)
plt.title("D1_Signal")

plt.subplot(4,2,3)
plt.xlim([0.5, 1])
plt.plot(timeAxis1,data1)
plt.title("D1_Signal ( 500ms - 1000ms )")

#Audio 2

plt.subplot(4,2,2)
plt.plot(data2)
plt.title("D2_Signal")

plt.subplot(4,2,4)
plt.xlim([0.5, 1])
plt.plot(timeAxis2,data2)
plt.title("D2_Signal ( 500ms - 1000ms )")

# sd.play(data)


# C.) and  D.)

#Audio 2
window2 = 0.1; # 100ms
soundLength2 = 2.5;
samples_in_window2 = samplerate2 / 10; # 2205

#Audio 1
window1 = 0.1; # 100ms
soundLength1 = 2.5;
samples_in_window1 = samplerate1 / 10; # 2205


#Audio 2
for i in range(11,25):
    startingSample = i *samples_in_window2
    startingSample = int(startingSample)
    slicedData = data2[startingSample:startingSample + int(samples_in_window2)]

    print(i," : " ,len(slicedData)," , samples : ",startingSample," - ", int(startingSample + samples_in_window2), i*100,"ms - ",(i+1) * 100,"ms")
    dft = fft(slicedData)

    #first and only plot
    if(i == 11):
        x_axis_for_sliced_data = np.arange(10*samples_in_window2 , 11*samples_in_window2) *T2
        print(x_axis_for_sliced_data)

        plt.subplot(4, 2, 6)
        plt.xlim([1, 1.1])
        plt.plot( x_axis_for_sliced_data,slicedData)
        plt.title("D2_Signal ( 1000ms - 1100ms )")

        plt.subplot(4, 2, 8)
        plt.ylim(0,12)
        plt.xlim([1, 1.1])
        plt.plot(x_axis_for_sliced_data, np.abs(dft))
        plt.title("D2_DFT Magnitude ( 1000ms - 1100ms )")



#Audio 1
for i in range(11, 25):
    startingSample = i * samples_in_window1
    startingSample = int(startingSample)
    slicedData = data1[startingSample:startingSample + int(samples_in_window1)]

    print(i, " : ", len(slicedData), " , samples : ", startingSample, " - ", int(startingSample + samples_in_window1),
          i * 100, "ms - ", (i + 1) * 100, "ms")
    dft = fft(slicedData)

    # first and only plot
    if (i == 11):
        x_axis_for_sliced_data = np.arange(10 * samples_in_window1, 11 * samples_in_window1) * T1
        print(x_axis_for_sliced_data)

        plt.subplot(4, 2, 5)
        plt.xlim([1, 1.1])
        plt.plot(x_axis_for_sliced_data, slicedData)
        plt.title("D1_Signal ( 1000ms - 1100ms )")

        plt.subplot(4, 2, 7)
        plt.xlim([1, 1.1])
        plt.plot(x_axis_for_sliced_data, np.abs(dft))
        plt.title("D1_DFT Magnitude ( 1000ms - 1100ms )")


plt.subplots_adjust(hspace=0.6)
plt.show()

# e.) Audio files are completely different, other one is harmonic sound, sample rate is the double and the other one is also 0.8 seconds longer
# furthermore, their freqs differ completely, so also the other ones dft magnitude is considerably higher