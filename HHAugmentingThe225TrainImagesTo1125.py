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
#selectedImages = pd.read_csv('selectedTrainImages.csv')
#all399TrainAnnotations = pd.read_csv('annotations_train_HHRNLB.csv')

trainImages=[]
#path='225HorizontalFlip/'+'name.JPG'
#print(path)
def allImages():
    for file in glob.glob("225Selected/*.JPG"):
        trainImages.append(file)

    for file in glob.glob("225Selected/*.Jpeg"):
        trainImages.append(file)
    print('Total number of test images in test folder is: ' + str(len(trainImages)))

def horizontalFlipImages():
    for image in trainImages:
        name = image
        name=name.split('\\')
        name = name[1].split('.')

        newNAME = name[0] + '-HorizontalFlip.' + name[1]
        print(newNAME)
        print(name)
        img = cv2.imread(image)
        img_h = cv2.flip(img, 1) #Horizontal flip - across the y axix

        path='225HorizontalFlip/'+newNAME
        cv2.imwrite(path, img_h)

def bothAxesFlipImages():
    for image in trainImages:
        name = image
        name = name.split('\\')
        name = name[1].split('.')

        newNAME = name[0] + '-BothAxesFlip.' + name[1]
        #print(newNAME)
        #print(name)
        img = cv2.imread(image)
        img_h = cv2.flip(img, -1)  # Horizontal flip - across the y axix

        path = '225BothAxesFlip/' + newNAME
        cv2.imwrite(path, img_h)

def verticalFlipImages():
    for image in trainImages:
        name = image
        name = name.split('\\')
        name = name[1].split('.')

        newNAME = name[0] + '-VerticalFlip.' + name[1]
        #print(newNAME)
        #print(name)
        img = cv2.imread(image)
        img_v = cv2.flip(img, 0)  # Vertical flip - across the X axix

        path = '225VerticalFlip/' + newNAME
        cv2.imwrite(path, img_v)
allImages()
#horizontalFlipImages()
#bothAxesFlipImages()
verticalFlipImages()

