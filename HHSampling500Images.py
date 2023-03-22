import glob, os
import pandas as pd
import csv
import shutil
#Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np
os.chdir("D:/PHD Data/Real NBL/images_handheld")
handHeldAnnotationsEdit2 = pd.read_csv('annotations_handheld_edit2.csv')

allImages=[]
sampled500Images=[]
sampledImages=[]
def getNamesofAllImagesInHandHeldFolder():
    for file in glob.glob("*.JPG"):
        allImages.append(file)

    for file in glob.glob("*.Jpeg"):
        allImages.append(file)
    print('Total number of NLB images before sampling 500 is:  : ' + str(len(allImages)))

def testingSampling():
    dummyImages=[]
    x=0
    y=1019
    while x<=y:
        if x%2==0:
            dummyImages.append(x)
        x+=1
    print(len(dummyImages))
    print(x)
def sample500Images():

    for image in allImages:
        if allImages.index(image)%2==0:
            sampledImages.append(image)

    print('Total number of sampled images is: '+str(len(sampledImages)))
    unsampled=list(set(allImages)-set(sampledImages))
    print('Total number of unsampled images to be deleted is: ' +str(len(unsampled)))
    return unsampled

def removeunsampledImagesAnnotationsFromCSV2():
    df_filtered = handHeldAnnotationsEdit2
    annotaionsfor1019B4Sampling=len(df_filtered)
    for image_Name in unsampledImagesToDelete:
        for _, row in df_filtered.iterrows():
            if row.filename == image_Name:
                df_filtered = df_filtered[(df_filtered['filename'] != image_Name)]

    print('Total number of annotations for the 1019 images before sampling is: '+ str(annotaionsfor1019B4Sampling))
    print('Total number of annotations for the 510 sampled images is: '+ str(len(df_filtered)))
    print('Total number of annotations for the 509 removed after sampling is: '+ str(annotaionsfor1019B4Sampling-len(df_filtered)))

    df_filtered.to_csv('annotations_handheld_edit3.csv', index=False)
    print(handHeldAnnotationsEdit2)
    print(df_filtered.head)

def moveUnsampledImages():
    for image in unsampledImagesToDelete:

        shutil.move(image, '509UnsampledImages/' + image)
#getNamesofAllImagesInHandHeldFolder()
#testingSampling()
#unsampledImagesToDelete=sample500Images()
#removeunsampledImagesAnnotationsFromCSV2()
#moveUnsampledImages()
