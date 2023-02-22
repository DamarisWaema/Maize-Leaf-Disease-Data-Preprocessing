import glob, os
import shutil

import pandas as pd
from PIL import Image
from numpy import random
from random import choice

os.chdir("D:/PHD Data/Real NBL/images_boom")
testAnnotationEdit8 = pd.read_csv('annotations_boom_edit8.csv')
testImages=[]
def getNamesofTestImagesFromTestFolder():
    for file in glob.glob("98TestImages/*.JPG"):
        image_Name = file.split("\\")
        image_Name = image_Name[1]
        testImages.append(image_Name)
    print('Total number of images in test folder is : ' + str(len(testImages)))
    #print(testImages[0])

def getNamesOfTestImagesInTestAnnotations():
    test_imageNames=testAnnotationEdit8.image_name.unique()
    print('Total number of images in test annotations csv is : ' + str(len(test_imageNames)))
    #print(test_imageNames[0])
    #train = set(train_imageNames)
    #print('Unique train images is: ' + str(len(train)))
    #trainImagesToRemove=set(train_imageNames)^set(trainImages)
    #print('Total number of images in train annotations csv to be removed is: ' + str(len(trainImagesToRemove)))
    #print(trainImagesToRemove)
    return test_imageNames

def getNamesOfImagesInTestFolderandNotInAnnotations():
    NamesOfImagesInTestFolderandNotInAnnotations=[]
    for name in testImages:
        if not(name in test_imageNamesInAnnotation):
            NamesOfImagesInTestFolderandNotInAnnotations.append(name)
    print('Number of images in test folder and not in test annotations is:  ' +str(len(NamesOfImagesInTestFolderandNotInAnnotations)))
    print(NamesOfImagesInTestFolderandNotInAnnotations)
    return NamesOfImagesInTestFolderandNotInAnnotations

def getNamesOfImagesInAnnotationsAndNotInTestFolder():
    names=[]
    for name in test_imageNamesInAnnotation:
        if not (name in testImages):
            names.append(name)
    print('Number of images in annotations and not in test folder is:  ' + str(
        len(names)))
    print(names)
    return names

getNamesofTestImagesFromTestFolder()
test_imageNamesInAnnotation=getNamesOfTestImagesInTestAnnotations()
NamesOfImagesInAnnotationsAndNotInTestFolder=getNamesOfImagesInAnnotationsAndNotInTestFolder()
NamesOfImagesInTestFolderandNotInAnnotations=getNamesOfImagesInTestFolderandNotInAnnotations()