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
        This class handles sorting of the Image Files. 
        The target of this package is to create an ???? image of the measurements, therefore the files need to be sorted corretly. 
        This is a challenge since these files have to be sorted according to the substrate concentrations in their path.

        args:
            folder: String; String which directs to the folder in which the measurement files are located
        returns:
            None
    '''

folder = pathlib.Path(r"F:\Juelich\soluble MP38.8.10") #in diesem Ordner liegen die Dateien, muss angepasst werden!
files = [file for file in folder.glob('*.nd2')] #hier werden die Datei namen der einzelen Dateien hinterlegt

newList = ["_0,05mM", "_0,075mM","_0,1mM", "_0,5mM", "_0,75mM", "_0,25mM", "_1mM", "_2,5mM", "_5mM", "_7,5mM", "_10mM", "_25mM", "_50mM", "_75mM", "_100mM", "_250mM", '_500mM', '750mM', '_1000mM']
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
