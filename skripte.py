from pims import ND2_Reader
import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import time
import re



folder = pathlib.Path(r"C:\Users\rieb\Desktop\Experiments\Mikroskopie\soluble MP38.8.10\Repetition") #in diesem Ordner liegen die Dateien, muss angepasst werden!
files = [file for file in folder.glob('*.nd2')] #hier werden die Datei namen der einzelen Dateien hinterlegt


fig, ax = plt.subplots(1,len(files), figsize = (20,4), dpi=150)

ergebnisse  = {}
ergebnisse2 = {}
images      = {}


list_concentration = ["0,05", "0,1"]

correct_list = []

for i in files:
    path = string = str(i)
    for j in list_concentration:
        ret = re.search(j, path)
        if ret != None:
            correct_list.append(i)
        else:
            print("oder auch nich")

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