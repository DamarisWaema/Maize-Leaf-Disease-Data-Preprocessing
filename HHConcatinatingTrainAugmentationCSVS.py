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

#os.chdir("D:/PHD Data/Real NBL/annotations") # Uncomment to concatenate dataframes
os.chdir("D:/PHD Data/Real NBL/all1800HHTrainImages") #comment to concatenate DFs
# addAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-ArithmeticAdd.csv')
# multiplyAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-ArithmeticMultiply.csv')
# gaussianAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-GaussianNoise.csv')
# HFAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-HF.csv')
# resizedAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-Resized.csv')
# rotateAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-Rotate-45To45.csv')
# ShearXAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-ShearX.csv')
# VFAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages-VF.csv')
trainImages=[]
trainAnnotations=pd.read_csv('all1800HHTrainAnnotations.csv')

# def concatenateAnnotations():
#     frames=[addAnnotations, multiplyAnnotations, gaussianAnnotations, HFAnnotations, resizedAnnotations, rotateAnnotations, ShearXAnnotations, VFAnnotations]
#     allAnnotations=pd.concat(frames, ignore_index=True)
#     allAnnotations.to_csv('all1800HHTrainAnnotations.csv', index=False)

def getTrainImages():
    for file in glob.glob("*.jpg"):
        trainImages.append(file)

def getUniqueNamesInTrainAnnotations():
    trainnames = trainAnnotations.filename.unique()
    print('Number of unique images in train annotations is: ' + str(len(trainnames)))
    print('Total number of train images in train folder is: ' + str(len(trainImages)))




#concatenateAnnotations()
getTrainImages()
getUniqueNamesInTrainAnnotations()

