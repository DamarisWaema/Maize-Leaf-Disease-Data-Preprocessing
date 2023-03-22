import glob, os
import pandas as pd
import cv2

import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/PHD Data/Real NBL/images_handheld")
handHeldAnnotations = pd.read_csv('annotations_handheld.csv')

allJPGImages = []
allJpegImages = []

allNoneNLBImages = []
uniqueNamesofNoneNLBImagesList = []
affectedJPGRows=[]
affectedJPEGRows=[]

def getNamesofAllImagesInHandHeldFolder():
    for file in glob.glob("*.JPG"):
        allJPGImages.append(file)
    for file in glob.glob("*.Jpeg"):
        allJpegImages.append(file)
    print('Total number of images in the handheld folder is: ' + str(len(allJPGImages)+len(allJpegImages)))
    print('Total number of JPG images in the handheld folder is: ' + str(len(allJPGImages)))
    print('Total number of Jpeg images in the handheld folder is: ' + str(len(allJpegImages)))



def addWidthHeightToHandHeldAnnotations():
    for file in glob.glob("*.JPG"):
        img = cv2.imread(file)
        dimensions = img.shape
        imageWidth = dimensions[1]
        imageHeight = dimensions[0]
        imageName = file
        #print(imageName)
        for _, row in handHeldAnnotations.iterrows():
            if(row.filename==imageName):
                handHeldAnnotations.loc[handHeldAnnotations["filename"] == imageName, "width"] = imageWidth
                handHeldAnnotations.loc[handHeldAnnotations["filename"] == imageName, "height"] = imageHeight
                affectedJPGRows.append('Affected')
    print('Done with JPG')
    for file in glob.glob("*.Jpeg"):
        img = cv2.imread(file)
        dimensions = img.shape
        imageWidth = dimensions[1]
        imageHeight = dimensions[0]
        imageName = file
        #print(imageName)
        for _, row in handHeldAnnotations.iterrows():
            if (row.filename == imageName):
                handHeldAnnotations.loc[handHeldAnnotations["filename"] == imageName, "width"] = imageWidth
                handHeldAnnotations.loc[handHeldAnnotations["filename"] == imageName, "height"] = imageHeight
                affectedJPEGRows.append('Affected')
    print('Done with Jpeg')
    print('Total number of annotations: '+ str(len(handHeldAnnotations)))

    print('Affected JPG rows: '+ str(len(affectedJPGRows)))
    print('Affected Jpeg rows: '+ str(len(affectedJPEGRows)))

    print(handHeldAnnotations.head)
    handHeldAnnotations.to_csv('annotations_handheld_edit1.csv', index=False)

#getNamesofAllImagesInHandHeldFolder()
#addWidthHeightToHandHeldAnnotations()