import glob, os
import shutil

import pandas as pd
from PIL import Image
from numpy import random
from random import choice

os.chdir("D:/PHD Data/Real NBL/images_boom")
trainAnnotationEdit7 = pd.read_csv('annotations_boom_edit7.csv')
testAnnotationEdit8 = pd.read_csv('annotations_boom_edit8.csv')
trainImages=[]
testImages=[]
def getNamesofTrainImagesFromTrainFolder():
    for file in glob.glob("392TrainImages/*.JPG"):
        image_Name = file.split("\\")
        image_Name = image_Name[1]
        trainImages.append(image_Name)
    print('Total number of images in train folderis : ' + str(len(trainImages)))
    #print(trainImages[0])




def getNamesOfTrainImagesInTrainAnnotations():
    train_imageNames=trainAnnotationEdit7.image_name.unique()
    print('Total number of images in train annotations csv is : ' + str(len(train_imageNames)))
    #print(train_imageNames[0])
    #train = set(train_imageNames)
    #print('Unique train images is: ' + str(len(train)))
    #trainImagesToRemove=set(train_imageNames)^set(trainImages)
    #print('Total number of images in train annotations csv to be removed is: ' + str(len(trainImagesToRemove)))
    #print(trainImagesToRemove)
    return train_imageNames

def getNamesOfImagesInTrainFolderandNotInAnnotations():
    NamesOfImagesInTrainFolderandNotInAnnotations=[]
    for name in trainImages:
        if not(name in train_imageNamesInAnnotation):
            NamesOfImagesInTrainFolderandNotInAnnotations.append(name)
    print('Number of images in train folder and not in train annotations is:  ' +str(len(NamesOfImagesInTrainFolderandNotInAnnotations)))
    print(NamesOfImagesInTrainFolderandNotInAnnotations)
    return NamesOfImagesInTrainFolderandNotInAnnotations

def getNamesOfImagesInAnnotationsAndNotInTrainFolder():
    names=[]
    for name in train_imageNamesInAnnotation:
        if not (name in trainImages):
            names.append(name)
    print('Number of images in annotations and not in train folder is:  ' + str(
        len(names)))
    print(names)
    return names
getNamesofTrainImagesFromTrainFolder()
train_imageNamesInAnnotation=getNamesOfTrainImagesInTrainAnnotations()
NamesOfImagesInAnnotationsAndNotInTrainFolder=getNamesOfImagesInAnnotationsAndNotInTrainFolder()
NamesOfImagesInTrainFolderandNotInAnnotations=getNamesOfImagesInTrainFolderandNotInAnnotations()