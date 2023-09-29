import glob, os
import pandas as pd
import cv2
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage

import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/PHD Data/Real NBL/annotations") # Uncomment to concatenate dataframes
addAnnotations = pd.read_csv('trainExtra50From5ORMore-ArithmeticAdd.csv')
multiplyAnnotations = pd.read_csv('trainExtra50From5ORMore-ArithmeticMultiply.csv')
HFAnnotations = pd.read_csv('trainExtra50From5ORMore-HF.csv')
resizedAnnotations = pd.read_csv('trainExtra50From5ORMore-Resized.csv')
ShearXAnnotations = pd.read_csv('trainExtra50From5ORMore-ShearX.csv')
VFAnnotations = pd.read_csv('trainExtra50From5ORMore-VF.csv')
speckleNoise=pd.read_csv('trainExtra50From5ORMore-SpeckleNoise.csv')
gaussianNoise=pd.read_csv('trainExtra50From5ORMore-GaussianNoise.csv')

rot90=pd.read_csv('trainExtra50From5ORMore-Rotate90.csv')
rot180=pd.read_csv('trainExtra50From5ORMore-Rotate180.csv')
rot270=pd.read_csv('trainExtra50From5ORMore-Rotate270.csv')
#trainImages=[]
#trainAnnotations=pd.read_csv('all1800HHTrainAnnotations.csv')
AllAnnotations = pd.read_csv('All550trainExtra50From5ORMore.csv')
def concatenateAnnotations():
    frames=[addAnnotations, multiplyAnnotations, HFAnnotations, resizedAnnotations, ShearXAnnotations, VFAnnotations, speckleNoise, rot90, rot180, rot270, gaussianNoise]
    allAnnotations=pd.concat(frames, ignore_index=True)
    allAnnotations.to_csv('All550trainExtra50From5ORMore.csv', index=False)

    print('Unique names: '+str(len(allAnnotations.filename.unique())))

    print('Total Number Of ANNOTATIONS FOR THE 550 IMages: ' + str(len(allAnnotations)))

def CorrectBoundingBoxes():
    print(AllAnnotations.head())

    for row in AllAnnotations.itertuples():
        AllAnnotations.at[row.Index, 'xmin'] = round(float(row.xmin))
        AllAnnotations.at[row.Index, 'ymin'] = round(float(row.ymin))
        AllAnnotations.at[row.Index, 'xmax'] = round(float(row.xmax))
        AllAnnotations.at[row.Index, 'ymax'] = round(float(row.ymax))

    AllAnnotations.to_csv('All550trainExtra50From5ORMore-edited.csv', index=False)
    print(AllAnnotations.head())

#concatenateAnnotations()
#CorrectBoundingBoxes()


