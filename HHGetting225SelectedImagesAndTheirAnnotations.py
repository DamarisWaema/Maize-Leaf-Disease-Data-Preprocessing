import glob, os
import pandas as pd
import cv2

import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/PHD Data/Real NBL/images_handheld/399TrainImages")
selectedImages = pd.read_csv('selectedTrainImages.csv')
all399TrainAnnotations = pd.read_csv('annotations_train_HHRNLB.csv')

allJPGImages = []
allJpegImages = []

def getNamesOfSelectedImages():
    images = selectedImages.imageName.unique()
    print('The number of 225 selected images is: ' +str(len(images)))
    return images
def copySelectedImagesToFolder():
    for image in selectedTrainImages:
        shutil.copy(image, '225Selected/' + image)

def getAnnotationsOfThe225SelectedImages():
    requiredAnnotations = []

    for image in selectedTrainImages:

        for row in all399TrainAnnotations.itertuples():
            if (row.filename == image):
                requiredAnnotations.append(row)
    df=pd.DataFrame(requiredAnnotations)


    print('The total number of annotations for the 225 images is: ' + str(len(requiredAnnotations)))
    print(df.head())
    print('Total number of unique images in the annotation file is: ' +str(len(df.filename.unique())))
    df.to_csv('annotationsFor225SelectedTrainImages.csv', index=False)
    return df.filename.unique()
#selectedTrainImages=getNamesOfSelectedImages()
#copySelectedImagesToFolder()
#namesInAnnotationFile=getAnnotationsOfThe225SelectedImages()
#missingNames=set(selectedTrainImages)-set(namesInAnnotationFile)
#print(missingNames)