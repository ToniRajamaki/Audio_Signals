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
import librosa.display
import IPython.display as ipd
CSVname = 'H283175.csv'
NUM_OF_FILTERS = 40

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

#Calculates averages and stds for each row in Mfccs and then combines them : [ ListOfMeans , ListOfStd ]
def CalcMeanAndStd(mfccs):
    averages = []
    stds = []
    for i in range(NUM_OF_FILTERS):
        mean_value = np.mean(mfccs[i])
        averages.append(mean_value)
        std_value = np.std(mfccs[i])
        stds.append(std_value)

    mean_and_std = averages + stds
    return mean_and_std


files = ReadCsvToDict(CSVname)
print(files)
for fileName in files:
    path = 'audio_files/'+fileName
    (signal, sr) = librosa.load(path, sr=None)
    mfccs = librosa.feature.mfcc(y=signal, n_mfcc=NUM_OF_FILTERS, sr=sr)
    mean_and_stds = CalcMeanAndStd(mfccs)

    print(mean_and_stds)
    break





