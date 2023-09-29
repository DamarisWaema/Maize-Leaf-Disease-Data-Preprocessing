
import glob, os
import pandas as pd
import cv2

import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/PHD Data/Real NBL/allFinal2575HHTrainData")
uploadedImages = pd.read_csv('uploaded.csv')
all2575Images = pd.read_csv('annotationsFor2575HHFinalTrainingData.csv')

def getNamesOfUnuploadedImamges():
    allimages=all2575Images.filename.unique()
    uploadedOnes=uploadedImages.filename.unique()
    print('Number of all Images: ' +str(len(allimages)))
    print('Number of uploaded images: ' +str(len(uploadedOnes)))
    unuploadedOnes=set(allimages) -set(uploadedOnes)
    print('Number of mages to upload: ' +str(len(unuploadedOnes)))
    return list(unuploadedOnes)

def copyImagesToUploadToAFolder():
    for image in imagesToUpload:
        shutil.copy(image, 'imagesToUpload/' + image)


imagesToUpload=getNamesOfUnuploadedImamges()

copyImagesToUploadToAFolder()