import numpy as np
import csv
from numpy import dot
from numpy.linalg import norm
import librosa.display
import matplotlib.pyplot as plt

CSVname = 'H283175.csv'
NUM_OF_FILTERS = 40
mean_n_std_map = {}

# STEP 0
# Creates a dictionary from given csv file in form [Audiofilename : [ list, of ,tags ] ]
# Also creates a list with audiofile names for easy indexin
def ReadCsvToDict(CSVname):

    files = {}
    audio_file_names = []
    with open(CSVname, 'r') as data:
        for line in csv.DictReader(data):
            fileName = line['fileName']
            # Changing file ending from .mp3 to .wav
            newFileName = fileName.replace('mp3', 'wav')
            tags = line['tags']
            tag_list = tags.split(",")
            files[newFileName] = tag_list
            audio_file_names.append(newFileName)
    return files,audio_file_names


# STEP 0
# Goes through all files and adds every unique tag to a list
def GetTags(files):
    all_tags = []
    for file in files:
        for tag in files[file]:
            if tag not in all_tags and tag != '':
                all_tags.append(tag)
    return all_tags


# STEP 1
#Calculates Mfcc for audio file and then calss for CalcMeanAndStd with mfcc
def CalcMfccsMeansAndStds(files):
    for fileName in files:
        path = 'audio_files/'+fileName
        (signal, sr) = librosa.load(path, sr=None) # reading audio file
        mfccs = librosa.feature.mfcc(y=signal, n_mfcc=NUM_OF_FILTERS, sr=sr) # calculating mfcc
        mean_and_stds = CalcMeanAndStd(mfccs)
        mean_n_std_map[fileName] = mean_and_stds
    return mean_n_std_map


# STEP 1
#Support function for 'CalcMfccsMeansAndStds' function, calculates std and mean of mfcc
def CalcMeanAndStd(mfccs):
    averages = []
    stds = []
    for i in range(NUM_OF_FILTERS):
        mean_value = np.mean(mfccs[i])
        averages.append(mean_value)
        std_value = np.std(mfccs[i])
        stds.append(std_value)

    mean_and_std = averages + stds # [Mean, std, Mean, std....] len = 2*NUM_OF_FILTERS
    return mean_and_std


# STEP 1
# Calculates simularity matrix based on mfccs means and stds
def CalcSimiliratyMatrix(mean_n_std_map):

    simularityMatrix = np.zeros((len(mean_n_std_map),len(mean_n_std_map)))

    row = 0
    for i in mean_n_std_map:
        column = 0
        for j in mean_n_std_map:
            #calculate Cosine Similarity between two files
            cos_sim = dot(mean_n_std_map[i], mean_n_std_map[j]) / (norm(mean_n_std_map[i]) * norm(mean_n_std_map[j]))
            simularityMatrix[row, column] = cos_sim  #Adding result to simularity matrix
            column = column + 1
        row = row + 1
    return simularityMatrix


# STEP 2
# Goes throug all the tags and combines adds to a list every file with common tag
# Expect if the value is 1
def Divides_simularity_values_to_each_tag(sim_matrix, audio_file_names):

    sim_values_for_each_tag = {}
    all_tags = GetTags(files)

        # Going through all the unique tags
    for tag in all_tags:
        # This is used to generate list of simularity values with the same tag
        sim_values_on_this_tag = []
        #Accessing to a list of simulatiry values
        for row in range(len(sim_matrix)):
            #Accessing a value in list
            for column in range(len(sim_matrix[row])):
                # These bools keep track if a current tag is found within the two
                # files that are being compared
                compared_tag_found = False
                primary_tag_found = False
                # Ignoring diagonal elements of matrix (value = 1)
                if column == row:
                    continue

                SimilarityValue = sim_matrix[row][column]

                # PRIMARY AUDIOFILE
                # Getting information on the primary audio file
                primary_audio_name = audio_file_names[row]
                primary_tags = files[primary_audio_name]
                #Checking if current tag is found in primary audios tags
                for primary_tag in primary_tags:
                    if primary_tag == tag:
                        primary_tag_found = True

                # SECONDARY AUDIOFILE
                compared_audio_name = audio_file_names[column]
                compared_audio_tags = files[compared_audio_name]
                # Checking the secondary compared audiofiles tags
                for compared_tag in compared_audio_tags:
                    if compared_tag == tag:
                        compared_tag_found = True


                # Checking if common tag was found between audio files
                if primary_tag_found == True and compared_tag_found == True:
                    sim_values_on_this_tag.append(SimilarityValue)

        # After the unique tag has been looped through, we add every simularity value to a map with key being
        # Corresponding tag
        sim_values_for_each_tag[tag] = sim_values_on_this_tag


    return sim_values_for_each_tag


#  STEP 2
# Calculates means for similarity values that has been divided by tag
def CalcMeansForEachTag(sim_values_for_each_tag):

    sim_mean_for_each_tag = {}
    for tag in sim_values_for_each_tag:
        if (len(sim_values_for_each_tag[tag]) > 0):
            mean_value = sum(sim_values_for_each_tag[tag]) / len(sim_values_for_each_tag[tag]) # mean
            sim_mean_for_each_tag[tag] = mean_value

    return sim_mean_for_each_tag


# STEP 3
# Calculates average similarity between files for all data
def CalcSimularityAverageOfAllData(sim_matrix):

    sum_of_values = 0
    elements_in_list = len(sim_matrix)
    # Going through list of files with common tag
    for list in sim_matrix:
        # Adding each value together
        for element in list:
            sum_of_values = sum_of_values + element
    sum_of_values = sum_of_values - elements_in_list # taking difference of numerator and amount of elements in list
    # to ignore diagonal simularity values

    #Taking difference of denumerator to ignore diagonal values
    avg = sum_of_values / ((elements_in_list * elements_in_list) - elements_in_list)
    return avg


# Just prints the results from each tags mean simularity and average similarity of all data
def PrintResults(sim_mean_for_each_tag, average_simularity_of_all_data):

    print("-------  SIMULARITY MEAN BY TAG  -------\n")
    for tag in sim_mean_for_each_tag:
        print(tag,"  :  ",sim_mean_for_each_tag[tag])
    print("\n----------------------------------------")
    print("\nAverage similarity of all data \n")
    print(average_simularity_of_all_data, "\n")
    print("----------------------------------------")


# Plots heatmap of simularity matrix
def PlotHeatMap(sim_matrix):
    plt.figure()
    plt.imshow(sim_matrix, cmap='hot')
    plt.title("Heat map of simularity matrix (all files compared to each other)")
    plt.colorbar()
    plt.show()
    print(audio_file_names[88])


# STEP0
files, audio_file_names = ReadCsvToDict(CSVname) # Generating map and a list

# STEP1
mean_n_std_map = CalcMfccsMeansAndStds(files)
sim_matrix = CalcSimiliratyMatrix(mean_n_std_map)

# STEP2
sim_values_for_each_tag = Divides_simularity_values_to_each_tag(sim_matrix, audio_file_names)
sim_mean_for_each_tag = CalcMeansForEachTag(sim_values_for_each_tag)

# STEP3
average_simularity_of_all_data = CalcSimularityAverageOfAllData(sim_matrix)

# Results
PrintResults(sim_mean_for_each_tag,average_simularity_of_all_data)
PlotHeatMap(sim_matrix)






