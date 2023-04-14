import glob, os
import pandas as pd
import cv2
from PIL import Image
import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/PHD Data/Real NBL/images_handheld/399TrainImages/225Selected")
handHeldAnnotations = pd.read_csv('annotationsFor225SelectedTrainImages.csv')
print(handHeldAnnotations.head())

all225Images = []

allNoneNLBImages = []
uniqueNamesofNoneNLBImagesList = []
affectedJPGRows=[]
affectedJPEGRows=[]

def getNamesofAllImagesInHandHeldFolder():
    for file in glob.glob("*.JPG"):
        all225Images.append(file)
    for file in glob.glob("*.Jpeg"):
        all225Images.append(file)
    print('Total number of images in the selected folder is: ' + str(len(all225Images)))

def convertAllImagesTojpg():
    for file in all225Images:
        image = Image.open(file)
        # Specifying the RGB mode to the image
        #image = image.convert('RGB')
        name=file.split('.')
        fullname=name[0]+'.jpg'
        # Converting an image from PNG to JPG format
        image.save("225Selectedjpgs/"+fullname)


def changeFilenameExtentionsInAnnotations():

    for _, row in handHeldAnnotations.iterrows():
        name1=row.filename
        name=row.filename.split('.')
        fullName=name[0]+'.jpg'
        if(row.filename==name1):
            handHeldAnnotations.loc[handHeldAnnotations["filename"] == name1, "filename"] = fullName
    print(handHeldAnnotations.head())
    handHeldAnnotations.to_csv('225Selectedjpgs/annotationsFor225SelectedTrainImages.csv', index=False)


getNamesofAllImagesInHandHeldFolder()
#convertAllImagesTojpg()
#changeFilenameExtentionsInAnnotations()

