import glob, os
import pandas as pd
from random import choice

import csv
import shutil
#Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np
os.chdir("D:/PHD Data/Real NBL/images_handheld")
trainAnnotations = pd.read_csv('annotations_handheld_edit4.csv')
testAnnotations = pd.read_csv('annotations_handheld_edit5.csv')

testImages=[]
trainImages=[]

def getTrainImages():
    for file in glob.glob("408TrainImages/*.JPG"):
        trainImages.append(file)

    for file in glob.glob("408TrainImages/*.Jpeg"):
        trainImages.append(file)
    print('Total number of train images in train folder is: ' + str(len(trainImages)))

def getTestImages():
    for file in glob.glob("102TestImages/*.JPG"):
        testImages.append(file)

    for file in glob.glob("102TestImages/*.Jpeg"):
        testImages.append(file)
    print('Total number of test images in test folder is: ' + str(len(testImages)))
def getUniquNamesInTrainAnnotations():
    trainnames=trainAnnotations.filename.unique()
    print('Number of unique images in train annotations is: ' +str(len(trainnames)))

def getUniquNamesInTestAnnotations():
    testnames=testAnnotations.filename.unique()
    print('Number of unique images in test annotations is: ' +str(len(testnames)))

#getTrainImages()
#getTestImages()
#getUniquNamesInTrainAnnotations()
#getUniquNamesInTestAnnotations()