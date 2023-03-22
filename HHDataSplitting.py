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
handHeldAnnotationsEdit3 = pd.read_csv('annotations_handheld_edit3.csv')

allImages=[]
testImages=[]
uniqueNamesofNoneNLBImagesList=[]


def getNamesofAll510Images():
    for file in glob.glob("*.JPG"):
        allImages.append(file)

    for file in glob.glob("*.Jpeg"):
        allImages.append(file)
    print('Total number of images before splitting is: ' + str(len(allImages)))

def splitData():
    n=102
    for i in range(n):
        testImage=choice(allImages)
        testImages.append(testImage)
        allImages.remove(testImage)

    print('The number of test images is: '+ str(len(testImages)))
    train_images=allImages
    print('The number of images to be used for training is: '+str(len(train_images)))

    return train_images

def copyImagesToRespectiveFolders():
    for image in testImages:
        shutil.copy(image, '102TestImages/' + image)

    for trainImg in trainImages:
        shutil.copy(trainImg, '408TrainImages/' + trainImg)
    print('Done copying images')


def getAnnotationsForTestAndTrainImages():
    totalAnnotationsFor510Images=len(handHeldAnnotationsEdit3)
    allAnnotationsfor510Images=handHeldAnnotationsEdit3
    df_filteredTrain = handHeldAnnotationsEdit3

    for image_Name in testImages:
        for _, row in df_filteredTrain.iterrows():
            if row.filename == image_Name:
                df_filteredTrain = df_filteredTrain[(df_filteredTrain['filename'] != image_Name)]
    print('Total number of annotations for the 510 images is: '+str(totalAnnotationsFor510Images))
    print('Total number of annotations for the 408 train images is: '+str(len(df_filteredTrain)))
    testimageAnnotations=pd.concat([allAnnotationsfor510Images,df_filteredTrain]).drop_duplicates(keep=False)
    print('Total number of annotations for the 102 test images is: '+str(len(testimageAnnotations)))
    print(testImages[0])
    print(testimageAnnotations.head)
    print(trainImages[0])

    print(df_filteredTrain.head)

    df_filteredTrain.to_csv('annotations_handheld_edit4.csv', index=False)
    testimageAnnotations.to_csv('annotations_handheld_edit5.csv', index=False)

#getNamesofAll510Images()
#trainImages=splitData()
#copyImagesToRespectiveFolders()
#getAnnotationsForTestAndTrainImages()