import glob, os
import shutil

import pandas as pd
from PIL import Image
from numpy import random
from random import choice

os.chdir("D:/PHD Data/Real NBL/images_boom")
allImages=[]
testImages=[]
boomAnnotationsEdit4 = pd.read_csv('annotations_boom_edit4.csv')

def getNamesofAllImagesInBoomFolder():
    for file in glob.glob("*.JPG"):
        image_Name = file.split(".")
        image_Name = image_Name[0]
        allImages.append(image_Name)
    print('Total number of images before data splitting is: ' + str(len(allImages)))


def splitData():
    n=98
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
        name = image + '.JPG'
        shutil.copy(name, '98TestImages/' + name)

    for image in trainImages:
        name = image + '.JPG'
        shutil.copy(name, '392TrainImages/' + name)
    print('Done copying images')

def getAnnotationsForTestImages():
    test_Images = []
    totalAnnotationsFor490Images=len(boomAnnotationsEdit4)
    allAnnotationsfor490Images=boomAnnotationsEdit4
    df_filteredTrain = boomAnnotationsEdit4
    for file in glob.glob("98TestImages/*.JPG"):
        tempTuple = os.path.splitext(file)
        image_Name = tempTuple[0]
        image_Name = image_Name.split("\\")
        image_Name = image_Name[1]
        test_Images.append(image_Name)

    for image_Name in test_Images:
        for _, row in df_filteredTrain.iterrows():
            if row.imageName == image_Name:
                df_filteredTrain = df_filteredTrain[(df_filteredTrain['imageName'] != image_Name)]
    #print(df_filteredTrain.head)
    print('Total number of annotations for the 490 images is: '+str(totalAnnotationsFor490Images))
    print('Total number of annotations for the 392 train images is: '+str(len(df_filteredTrain)))
    testimageAnnotations=pd.concat([allAnnotationsfor490Images,df_filteredTrain]).drop_duplicates(keep=False)
    print('Total number of annotations for the 98 test images is: '+str(len(testimageAnnotations)))
    #print(testimageAnnotations.head)
    #print(test_Images[0])

    df_filteredTrain.to_csv('annotations_boom_edit5.csv', index=False)
    testimageAnnotations.to_csv('annotations_boom_edit6.csv', index=False)

#getNamesofAllImagesInBoomFolder()
#trainImages=splitData()
#copyImagesToRespectiveFolders()
getAnnotationsForTestImages()
