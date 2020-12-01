import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sounddevice as sd
import time
from scipy.io import wavfile
from scipy.fftpack import fft
import csv

from numpy import dot
from numpy.linalg import norm
import librosa
import librosa.display
import IPython.display as ipd
from scipy.spatial import distance
CSVname = 'H283175.csv'
NUM_OF_FILTERS = 40
mean_n_std_map = {}

#Creates a dictionary from given csv file in form [Audiofilename : [ list, of ,tags ] ]
files_n = 11
def ReadCsvToDict(CSVname):
    files = {}
    counter = 0
    with open(CSVname, 'r') as data:
        for line in csv.DictReader(data):
            counter = counter + 1
            if counter == files_n:
                break

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


def CalcSimiliratyMatrix(mean_n_std_map):

    simularityMatrix = np.zeros((len(mean_n_std_map),len(mean_n_std_map)))
    row = 0


    for i in mean_n_std_map:
        column = 0
        print("row: ",row)
        for j in mean_n_std_map:
            #calculate Cosine Similarity
            cos_sim = dot(mean_n_std_map[i], mean_n_std_map[j]) / (norm(mean_n_std_map[i]) * norm(mean_n_std_map[j]))
            simularityMatrix[row, column] =cos_sim

            print(column)
            column = column + 1
        row = row + 1
    return simularityMatrix
files = ReadCsvToDict(CSVname)

for fileName in files:
    path = 'audio_files/'+fileName
    (signal, sr) = librosa.load(path, sr=None)
    mfccs = librosa.feature.mfcc(y=signal, n_mfcc=NUM_OF_FILTERS, sr=sr)
    mean_and_stds = CalcMeanAndStd(mfccs)
    mean_n_std_map[fileName] = mean_and_stds


sim_matrix = CalcSimiliratyMatrix(mean_n_std_map)
print(sim_matrix)




