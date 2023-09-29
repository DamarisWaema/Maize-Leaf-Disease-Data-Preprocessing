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
addAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-ArithmeticAdd.csv')
multiplyAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-ArithmeticMultiply.csv')
gaussianAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-GaussianNoise.csv')
HFAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-HF.csv')
resizedAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-Resized.csv')
rotate270ShotNoise = pd.read_csv('annotationsFor225SelectedTrainImages-Rotate270ShotNoise.csv')
rot90 = pd.read_csv('annotationsFor225SelectedTrainImages-Rotate90.csv')
rot180 = pd.read_csv('annotationsFor225SelectedTrainImages-Rotate180.csv')

VFAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-VF.csv')
AllAnnotations= pd.read_csv('all2025HHTrainAnnotations.csv')
maxPool=pd.read_csv('aTest-Resized-Maxpooling2.csv')
def concatenateAnnotations():
    frames=[addAnnotations, rot180, multiplyAnnotations, gaussianAnnotations, HFAnnotations, resizedAnnotations, rotate270ShotNoise, rot90, VFAnnotations]
    allAnnotations=pd.concat(frames, ignore_index=True)
    allAnnotations.to_csv('all2025HHTrainAnnotations.csv', index=False)

def CorrectBoundingBoxes():
    print(maxPool.head())

    for row in maxPool.itertuples():
        maxPool.at[row.Index, 'xmin'] = round(float(row.xmin))
        maxPool.at[row.Index, 'ymin'] = round(float(row.ymin))
        maxPool.at[row.Index, 'xmax'] = round(float(row.xmax))
        maxPool.at[row.Index, 'ymax'] = round(float(row.ymax))

    maxPool.to_csv('annotationsTest-Resized-Maxpooling.csv', index=False)
    print(maxPool.head())
    print(len(maxPool.filename.unique()))
#concatenateAnnotations()
CorrectBoundingBoxes()


