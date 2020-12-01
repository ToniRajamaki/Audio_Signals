import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sounddevice as sd
import time
from scipy.io import wavfile
from scipy.fftpack import fft
import csv
import librosa
CSVname = 'H283175.csv'

#Creates a dictionary from given csv file in form [Audiofilename : [ list, of ,tags ] ]
def ReadCsvToDict(CSVname):
    files = {}
    with open(CSVname, 'r') as data:
        for line in csv.DictReader(data):


            mystr = line['fileName']
            # Changing file ending from .mp3 to .wav
            newstr = mystr.replace('mp3', 'wav')

            tags = line['tags']
            tag_list = tags.split(",")
            files[newstr] = tag_list
    return files

# def GetWavWithPath(path):

files = ReadCsvToDict(CSVname)
print(files)
for fileName in files:
    path = 'audio_files/'+fileName
    (signal, rate) = librosa.load(path, sr=None)
    break

plt.figure()
plt.plot(signal)
plt.title(rate)
plt.show()




