import librosa
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sounddevice as sd
import time
from scipy.io import wavfile
from scipy.fftpack import fft
from librosa import display


def data_to_spec(data):
    D = librosa.stft(data)
    return librosa.power_to_db(np.abs(D)**2, ref=np.median)

def plot_power_freq(signal, N, fs):
    N = signal.shape[0]  # number of data points

    time = np.arange(0, float(N), 1) / fs  # create a time variable in seconds
    print(time)

    k = np.fft.rfftfreq(N)  # generate frequency values
    freq = k / fs  # normalize them

    # freq = np.arange(0, (N/2), 1.0) * (rate*1.0/N);
    # fft to get the power
    power = (np.fft.rfft(signal))

    # normalize (so that the length doesn't matter)
    power = power / N

    # apply Hann window and take the FFT
    win = np.hanning(N)
    windowed_power = (np.fft.rfft(win * signal))
    windowed_power = windowed_power / N
    # plot power(in db) against frequency (in khz)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(freq / 1000, 10 * np.log10(power ** 2), linewidth=0.2)
    plt.xlabel('Frequency (kHz)')
    plt.ylabel('Power (dB)')
    plt.title('FFT only')
    plt.subplot(212)
    plt.plot(freq / 1000, 10 * np.log10(windowed_power ** 2), linewidth=0.2)
    plt.xlabel('Frequency (kHz)')
    plt.ylabel('Power (dB)')
    plt.title('Hanning Window + FFT')

    plt.show()

#Audio 1
samplerate1, audio1 = wavfile.read('audio1.wav')  # Fs : 44100 |  samples: 145530  | time = 3.3s
print(samplerate1,"   ", len(audio1))
T2 = 1/samplerate1 #time for one sample
window2 = 0.1 # 100ms
soundLength2 = 2.5
samples_in_window1 = samplerate1 / 10;# 4410
N1 = 145530



def p():
    hanning_whole_data = np.array(0)
    for i in range(0,33):
        # boundaries for data windowing
        startingSample = i *samples_in_window1
        startingSample = int(startingSample)
        print(i, ":  |      samples : ", startingSample, " - ", int(startingSample + samples_in_window1), "        |   ",
              i * 100, "ms - ", (i + 1) * 100, "ms")

        windowData = audio1[startingSample:startingSample + int(samples_in_window1)] # Rectangular data (original data)
        hanning_windhowData = windowData * np.hanning(samples_in_window1)

        hanning_whole_data = np.hstack((hanning_whole_data,hanning_windhowData))

        dft = fft(windowData)
        hanning_dft = fft(hanning_windhowData)

        #first and only plot
        if(i == 11):


            x_axis_for_sliced_data = np.arange(i-1*samples_in_window1 , i*samples_in_window1) *T2
            print(x_axis_for_sliced_data)
            plt.subplot(2, 1, 1)
            plt.xlim([1, 1.1])
            plt.plot(x_axis_for_sliced_data,windowData)
            plt.title("Rectangular windowing ( 1000ms - 1100ms )")

            plt.subplot(2, 1, 2)
          #  plt.ylim(0,12)
            plt.xlim([1, 1.1])
            plt.plot(x_axis_for_sliced_data, hanning_windhowData)
            #plt.plot(x_axis_for_sliced_data, np.abs(dft),title = "hanning windowing")
            plt.title("Hanning windowing ( 1000ms - 1100ms )")
            #plt.show()

            plt.figure() ##Trying to plot sum signals
            x_axis_for_sliced_data = np.arange(i - 2 * samples_in_window1, i -1 * samples_in_window1) * T2
            plt.subplot(1,3,1)
            plt.plot(x_axis_for_sliced_data, hanning_windhowData)  #1

            x_axis_for_sliced_data = np.arange(i - 1 * samples_in_window1, i  * samples_in_window1) * T2
            plt.subplot(1, 3, 2)
            plt.plot(x_axis_for_sliced_data, hanning_windhowData)  # 2

            x_axis_for_sliced_data = np.arange(i  * samples_in_window1, i + 1 * samples_in_window1) * T2
            plt.subplot(1, 3, 3)
            plt.plot(x_axis_for_sliced_data, hanning_windhowData)  # 3



    plt.figure()
    plt.subplot(211)
    print(audio1)
    plt.plot(abs(fft(audio1)))
    plt.title("Original dft signal")

    plt.subplot(212)
    plt.plot(abs(fft(hanning_whole_data)))
    plt.title("hanning windowed signal")
    #plt.show()

    # plot_power_freq(audio1,145530,44100)
    y, sr = librosa.load("audio1.wav", sr=None)
    S = np.abs(librosa.stft(y,window="hann"))
    S2 = librosa.stft(y,window="hann")
    o_s = librosa.istft(S2)

    fig = plt.figure()

    #img = librosa.display.specshow(librosa.amplitude_to_db(S))
    # plt.title('Power spectrogram')
    # fig.colorbar(img, format="%+2.0f dB")
    plt.subplot(211)
    plt.plot(S)
    plt.subplot(212)
    plt.plot(o_s,Linewidth=0.15)



    plt.show()

p()





