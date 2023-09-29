import glob, os
import pandas as pd
import cv2

import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/PHD Data/AnnotationsToEdit")
# annotations = pd.read_csv('annotationsFor2575HHFinalTrainingData.csv')
annotations = pd.read_csv('annotationsTest-Maxpooling.csv')


def changeNames():
    for row in annotations.itertuples():
        name=row.filename
        new=name.split('-MaxPooling.jpg')
        newname=new[0]+'-CV2Norm-MP.jpg'
        annotations.at[row.Index, 'filename'] = newname
    print(annotations.head())
    annotations.to_csv('annotationsTest-CV2Norm-MP.csv', index=False)

# def CorrectBoundingBoxes():
#     print(maxPool.head())
#
#     for row in maxPool.itertuples():
#         maxPool.at[row.Index, 'xmin'] = round(float(row.xmin))
#         maxPool.at[row.Index, 'ymin'] = round(float(row.ymin))
#         maxPool.at[row.Index, 'xmax'] = round(float(row.xmax))
#         maxPool.at[row.Index, 'ymax'] = round(float(row.ymax))
#
#     maxPool.to_csv('annotationsTest-666-final.csv', index=False)
#     print(maxPool.head())
#     print(len(maxPool.filename.unique()))

changeNames()
# CorrectBoundingBoxes()

