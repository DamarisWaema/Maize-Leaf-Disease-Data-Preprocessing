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
handHeldAnnotations = pd.read_csv('annotations_handheld_edit2.csv')

allImages=[]
images5OrMoreAnnotations=[]

def getNamesofAllImagesInHandHeldFolder():
    for file in glob.glob("*.JPG"):
        allImages.append(file)

    for file in glob.glob("*.Jpeg"):
        allImages.append(file)
    print('Total number of images before deleting none NLB ones is: ' + str(len(allImages)))
def getNamesOf5OrMoreAnnotationsImages():
    annotationsFor5OrMoreAnnotationsImages = 0
    for image_Name in allImages:
        annotaions=  len(handHeldAnnotations[handHeldAnnotations["filename"]==image_Name])

        if annotaions>=5:
            annotationsFor5OrMoreAnnotationsImages=annotationsFor5OrMoreAnnotationsImages+annotaions
            images5OrMoreAnnotations.append(image_Name)
    print('Total number of images with >=5 annotations is: ' + str(len(images5OrMoreAnnotations)))
    print('Images to be left after deleting those with 5 or more annotations is: '+ str(len(allImages)-len(images5OrMoreAnnotations)))
    print('Total number of annotations for the remaining 1019 images is: '+str(len(handHeldAnnotations)))

    print('Total number of annotations for images with 5 or more annotations is: '+str(annotationsFor5OrMoreAnnotationsImages))
    print('Total number of annotations to remain after deleting those for images with 5 or more annotations is: ' +str(len(handHeldAnnotations)-annotationsFor5OrMoreAnnotationsImages))

def moveImageswith5OrMoreAnnotations():
    for image_Name in images5OrMoreAnnotations:
        shutil.move(image_Name, 'images5OrMoreAnnotations/' + image_Name)

def deleteAnnotationsForImagesWith5OrMoreAnnotations():
    df_filtered = handHeldAnnotations

    for image_Name in images5OrMoreAnnotations:
        for _, row in df_filtered.iterrows():
            if row.filename == image_Name:
                df_filtered = df_filtered[(df_filtered['filename'] != image_Name)]
    print(df_filtered.head)
    df_filtered.to_csv('annotations_handheld_edit3.csv', index=False)

#getNamesofAllImagesInHandHeldFolder()
#getNamesOf5OrMoreAnnotationsImages()
#moveImageswith5OrMoreAnnotations()
#deleteAnnotationsForImagesWith5OrMoreAnnotations()