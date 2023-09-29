import glob, os
import pandas as pd
import cv2

import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/PHD Data/Real NBL/final80Testing_Resize/New")
handHeldAnnotations=pd.read_csv('annotationsTest-Resized.csv')
affectedImages=[]
affectedRows=[]

def correctingBBAnnotationsForTheRemaining499Images():
    for row in handHeldAnnotations.itertuples():
        if (row.x1 > row.x2):
            handHeldAnnotations.at[row.Index, 'x1'] = row.x2
            handHeldAnnotations.at[row.Index, 'x2'] = row.x1
            affectedImages.append(row.filename)

        if (row.y1 > row.y2):
            handHeldAnnotations.at[row.Index, 'y1'] = row.y2
            handHeldAnnotations.at[row.Index, 'y2'] = row.y1
            affectedImages.append(row.filename)

    print('The affected number of images is: ' + str(len(set(affectedImages))))
    print(affectedImages[0])
    print(list(set(affectedImages)))
    print('New annotations')
    print(handHeldAnnotations.head)
    handHeldAnnotations.to_csv('annotations_handheld_edit4.csv', index=False)


#correctingBBAnnotationsForTheRemaining499Images()