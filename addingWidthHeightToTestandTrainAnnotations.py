import glob, os
import shutil
import cv2
import pandas as pd
from PIL import Image
from numpy import random
from random import choice

os.chdir("D:/PHD Data/Real NBL/images_boom")
trainAnnotationEdit7 = pd.read_csv('annotations_boom_edit7.csv')
testAnnotationEdit8 = pd.read_csv('annotations_boom_edit8.csv')
trainImages=[]
def getNamesofTrainImagesFromTrainFolder():
    for file in glob.glob("392TrainImages/*.JPG"):
        image_Name = file.split("\\")
        image_Name = image_Name[1]
        trainImages.append(image_Name)
    print('Total number of images in train folderis : ' + str(len(trainImages)))
def addWidthHeightToTrainAnnotations():

    for file in glob.glob("392TrainImages/*.JPG"):
        img = cv2.imread(file)
        dimensions = img.shape
        imageWidth = dimensions[1]
        imageHeight = dimensions[0]
        imageName = file.split("\\")
        imageName = imageName[1]
        for _, row in trainAnnotationEdit7.iterrows():

                # trainAnnotationEdit7['width'] = trainAnnotationEdit7['width'].replace([row.width], imageWidth)
                # trainAnnotationEdit7['height'] = trainAnnotationEdit7['height'].replace([row.height], imageHeight)
            trainAnnotationEdit7.loc[trainAnnotationEdit7["image_name"] == imageName, "width"] = imageWidth
            trainAnnotationEdit7.loc[trainAnnotationEdit7["image_name"] == imageName, "height"] = imageHeight
    print(trainAnnotationEdit7.head)
    trainAnnotationEdit7.to_csv('annotations_boom_edit9.csv', index=False)

def addWidthHeightToTestAnnotations():
    for file in glob.glob("98TestImages/*.JPG"):
        img = cv2.imread(file)
        dimensions = img.shape
        imageWidth = dimensions[1]
        imageHeight = dimensions[0]
        imageName = file.split("\\")
        imageName = imageName[1]
        for _, row in testAnnotationEdit8.iterrows():

                # trainAnnotationEdit7['width'] = trainAnnotationEdit7['width'].replace([row.width], imageWidth)
                # trainAnnotationEdit7['height'] = trainAnnotationEdit7['height'].replace([row.height], imageHeight)
            testAnnotationEdit8.loc[testAnnotationEdit8["image_name"] == imageName, "width"] = imageWidth
            testAnnotationEdit8.loc[testAnnotationEdit8["image_name"] == imageName, "height"] = imageHeight
    print(testAnnotationEdit8.head)
    testAnnotationEdit8.to_csv('annotations_boom_edit10.csv', index=False)

#getNamesofTrainImagesFromTrainFolder()
#addWidthHeightToTrainAnnotations()
addWidthHeightToTestAnnotations()

# img = Image.open('392TrainImages/DSC00972_0.JPG')
#
# width, height=img.size
# print('width: '+ str(width ))
# print('height: ' +str(height))
# print(img.size)
# print('OpenCV values')
# img = cv2.imread('392TrainImages/DSC00972_0.JPG')
# dimensions = img.shape
# widthCV=dimensions[1]
# heightCV=dimensions[0]
# print('Open CV Values below: h, w, c')
# print(dimensions)
# print('width CV: '+ str(widthCV ))
# print('height CV: ' +str(heightCV))
#imageName = img.split('\\')
#imageName = imageName[1]
#trainAnnotationEdit7.loc[trainAnnotationEdit7["image_name"] == imageName, "width"] = imageWidth
#trainAnnotationEdit7.loc[trainAnnotationEdit7["image_name"] == imageName, "height"] = imageHeight
#print(trainAnnotationEdit7.head)
