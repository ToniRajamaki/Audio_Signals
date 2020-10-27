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


samplerate, data = wavfile.read('audio2.wav')
plt.plot(data)

plt.show()


# sd.play(data)