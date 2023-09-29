import glob, os
import pandas as pd
import cv2

import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/PHD Data/Real NBL/images_handheld/images5OrMoreAnnotations/Test")
#handHeldAnnotations=pd.read_csv('train.csv')
handHeldAnnotations=pd.read_csv('test.csv')

affectedImages=[]
affectedRows=[]

def correctingTrainBBAnnotations():
    for row in handHeldAnnotations.itertuples():
        if (row.x1 > row.x2):
            handHeldAnnotations.at[row.Index, 'x1'] = row.x2
            handHeldAnnotations.at[row.Index, 'x2'] = row.x1
            affectedImages.append(row.filename)

        if (row.y1 > row.y2):
            handHeldAnnotations.at[row.Index, 'y1'] = row.y2
            handHeldAnnotations.at[row.Index, 'y2'] = row.y1
            affectedImages.append(row.filename)

    #print('The affected number of images is: ' + str(len(set(affectedImages))))
    #print(affectedImages[0])
    #print(list(set(affectedImages)))
    #print('New annotations')
    #print(handHeldAnnotations.head)
    #handHeldAnnotations.to_csv('train-edited.csv', index=False)

def correctingTestBBAnnotations():
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
    #print(affectedImages[0])
    #print(list(set(affectedImages)))
    #print('New annotations')
    #print(handHeldAnnotations.head)
    handHeldAnnotations.to_csv('test-edited.csv', index=False)

#correctingTrainBBAnnotations()
#correctingTestBBAnnotations()