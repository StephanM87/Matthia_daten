#from pims import ND2_Reader
import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import time
import re


class FileSorter:

    '''
        This class handles thawdawdwdadwawdawdawdawdawadwdawdawdawdawdawdawdawdawdawdae sorting of the Image Files. 
        The target of this package is to create an ???? image of the measurements, therefore the files need to be sorted corretly. 
        This is a challenge since these files have to be sorted according to the substrate concentrations in their path.

        args:
            folder: String; String which directs to the folder in which the measurement files are located
Stephan iost der Beste
        returns:
            None
    '''

    def __init__(self, folder):
        self.folder = folder

    
    def upload_files(self):
        '''
            uploads the measurement files from the local storage and returns an unsorted list with the measurement files

            args:
                folder: String; String which directs to the folder in which the measurement files are located
            
            returns:
                files: List; List containing the unsorted files

        '''
        folder = pathlib.Path(repr(self.folder))
        files = [file for file in folder.glob('*.nd2')] #hier werden die Datei namen der einzelen Dateien hinterlegt
        return files

    def sorting_strings(self):

        '''
            Defines the regular expression list which should be screened for

            args:
                None
            
            returns:
                reg_expression: List; returns list with search patterns

        '''
        reg_expression = ["_0,1mM", "_0,5mM", "_0,75mM" "_0,25mM", "_0,05mM", "_0,075mM", "_1mM", "_2,5mM", "_5mM", "_7,5mM", "_10mM", "_25mM", "_50mM", "_75mM", "_100mM", "_250mM"]

        return reg_expression

    
    





folder = pathlib.Path(r"F:\Juelich\soluble MP38.8.10") #in diesem Ordner liegen die Dateien, muss angepasst werden!
files = [file for file in folder.glob('*.nd2')] #hier werden die Datei namen der einzelen Dateien hinterlegt


fig, ax = plt.subplots(1,len(files), figsize = (20,4), dpi=150)

ergebnisse  = {}
ergebnisse2 = {}
images      = {}


list_concentration = ["^0,001$", "^0,0025$", "0,005", "0,0075", "0,01", "0,025", "0,05", "0,075", "0,1", "0,25", "0,5", "0,75", "1", "2,5", "5", "7,5", "10", "25", "50", "75", "100", "250", "500", "750", "1000"]

newList = ["_0,1mM", "_0,5mM", "_0,75mM" "_0,25mM", "_0,05mM", "_0,075mM", "_1mM", "_2,5mM", "_5mM", "_7,5mM", "_10mM", "_25mM", "_50mM", "_75mM", "_100mM", "_250mM"]


correct_list = []

for i in newList:
    #path: str = str(i)
    #print(path)
    for j in files:
        path_string=str(j)
        path = repr(path_string) 
        print(path)
        ret = re.search(i, path)
        print(ret)
        if ret != None:
            correct_list.append(j)
            print(i)
        else:
            None

print(correct_list, "die richtige liste")

        



unsorted_files = []
for i in files:
    # c_date is the creation date of the respective file
    c_date = time.ctime(os.path.getctime(i))
    # path is the element of the list
    path = i
    string = str(i)
    # Regular expressions
    string = str(i)
    ret = re.search("0,05", string)
    #print(ret)

    new_entry = {}
    new_entry["date"] = c_date
    new_entry["path"] = path
    unsorted_files.append(new_entry)

#sorted_files = unsorted_files.sort(key=date, reverse=False)

sorted_files= sorted(unsorted_files, key=lambda d: d['date'])







for i in files:
    string = str(i)
    ret = re.search("0,05", string)
    ret01 = re.search("0,1", string)
    if ret != None:
        None
        #print(ret, "0,05 konzentration")

    elif ret01!=None:
        None
        #print(ret01, "0,1 konzentration")
    

    





'''
for i in range(len(files)):
    date = time.ctime(os.path.getctime(files[i]))
    print(date)
    frames= ND2_Reader(files[i])   # kann nd2 dateien lesen
    phase = frames.get_frame_2D(c=3) # holt aus der datei den ensprechenden Kanal (c) raus
    intens =frames.get_frame_2D(c=0)
    mask = intens< 0.03
    # Erzeugt eine Maske basierend auf den Intensitäten, bei der alles True is, 
                                    #das zu groß ist 
    phase[mask]=0
    #phase[mask]= np.nan
    ax[i].imshow(phase, cmap ="viridis") # Bild darstellen
    ax[i].axis("off")                    #Achsen ausblenden
    ergebnisse2[i] = np.nanmean(phase)
    ergebnisse[i] = np.nanmedian(phase)
    images[i]=phase
fig.savefig("test.png")
'''
