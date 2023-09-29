import glob, os
import pandas as pd
import csv
from PIL import Image
import cv2

import shutil
#Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np
os.chdir("D:/PHD Data/Real NBL/images_handheld/allImages/NLB/jpgs")
# allAnnotations = pd.read_csv('annotations_handheld.csv')
# nonNLBAnnotations = pd.read_csv('nonNLBImages.csv')
annotations=pd.read_csv('annotations_NLBjpgs.csv')


allNoneNLBImages=[]
uniqueNamesofNoneNLBImagesList=[]


def getNamesofAllNonNLBImagesInHandHeldFolder():
    for file in glob.glob("*.JPG"):
        allNoneNLBImages.append(file)

    for file in glob.glob("*.Jpeg"):
        allNoneNLBImages.append(file)
    print('Total number of images before deleting none NLB ones is: ' + str(len(allNoneNLBImages)))
    # df = pd.DataFrame(allNoneNLBImages)
    # df.to_csv('nonNLBImages.csv', index=False)
#Looking into the data to find out number of images that have no NLB

# def getNLBImages():
#     allimages = allAnnotations.filename.unique()
#     nonNLB = nonNLBAnnotations.filename.unique()
#     NLB=list(set(allimages) -set(nonNLB))
#     print('Number of mages to upload: ' +str(len(NLB)))
#     for image in NLB:
#         shutil.copy(image, 'NLB/' + image)

def convertImagesToJPG():
    for file in allNoneNLBImages:
        image = Image.open(file)
        # Specifying the RGB mode to the image
        #image = image.convert('RGB')
        name=file.split('.')
        fullname=name[0]+'.jpg'
        # Converting an image from PNG to JPG format
        image.save("jpgs/"+fullname)
def changesize():
    for file in allNoneNLBImages:
        image = Image.open(file)
        resized = image.resize((1333,1333))
        resized.save("1333 by 1333/"+file)


# def gettingannotationsOf1019():
#     nonNLB = nonNLBAnnotations.filename.unique()
#     print("non nlb: "+ str(len(nonNLB)))
#     allAnnotations = pd.read_csv('annotations_handheld.csv')
#
#     df_filtered=allAnnotations
#
#     for image in nonNLB:
#         for _, row in allAnnotations.iterrows():
#             if row.filename == image:
#                 allAnnotations = allAnnotations[(allAnnotations['filename'] != image)]
#     print("non nlb: "+ str(len(allAnnotations.filename.unique())))
#
#     print(allAnnotations.head)
#
#     allAnnotations.to_csv('annotations_NLB.csv', index=False)


def addDimentions():
    for file in glob.glob("*.jpg"):
        img = cv2.imread(file)
        dimensions = img.shape
        imageWidth = dimensions[1]
        imageHeight = dimensions[0]
        for _, row in annotations.iterrows():

                # trainAnnotationEdit7['width'] = trainAnnotationEdit7['width'].replace([row.width], imageWidth)
                # trainAnnotationEdit7['height'] = trainAnnotationEdit7['height'].replace([row.height], imageHeight)
            annotations.loc[annotations["filename"] == file, "width"] = imageWidth
            annotations.loc[annotations["filename"] == file, "height"] = imageHeight
    print(annotations.head)
    annotations.to_csv('annotations_NLB3.csv', index=False)

def changeExtentions():
    for _, row in annotations.iterrows():
        name1 = row.filename
        name = row.filename.split('.')
        fullName = name[0] + '.jpg'
        if (row.filename == name1):
            annotations.loc[annotations["filename"] == name1, "filename"] = fullName
    #print(handHeldAnnotations.head())
    #annotations.to_csv('annotations_NLBjpgs.csv', index=False)


getNamesofAllNonNLBImagesInHandHeldFolder()

#getNLBImages()
#convertImagesToJPG()
#changesize()
#gettingannotationsOf1019()
#changeExtentions()
addDimentions()