import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sounddevice as sd
import time
from scipy.io import wavfile
from scipy.fftpack import fft



A = np.ones(10)
A = A.astype(int)
print(A)
B = A * 2;
print(B)

D = np.zeros(30)
C = np.concatenate((A,B))
print(C)

