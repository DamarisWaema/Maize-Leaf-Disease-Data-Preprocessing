import glob, os
import pandas as pd
import csv
import shutil
#Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np
os.chdir("D:/PHD Data/Real NBL/images_boom")
boomAnnotations = pd.read_csv('annotations_boom.csv')

allImages=[]
allNoneNLBImages=[]
uniqueNamesofNoneNLBImagesList=[]

#Getting Names of All images in the boom folder
def getNamesofAllImagesInBoomFolder():
    for file in glob.glob("*.JPG"):
        allImages.append(file)
    print('Total number of images before deleting none NLB ones is: ' + str(len(allImages)))
#Looking into the data to find out number of images that have no NLB
def getNamesOfAllNoneNLBImages():
    for _, row in boomAnnotations.iterrows():
        if row.xmin == 0 and row.ymin ==0 and row.xmax == 0 and row.ymax ==0:
            image_Name=row.imageName+'.JPG'
            allNoneNLBImages.append(image_Name)
    # converting list to set to get unique names/remove duplicates
    uniqueNamesofNoneNLBImagesSet = set(allNoneNLBImages)
    uniquelist=list(uniqueNamesofNoneNLBImagesSet)
    print('Total number of rows that have no NLB is: ' + str(len(allNoneNLBImages)))
    print('Total number of images that have no NLB is: ' + str(len(uniquelist)))
    print('Total number of images that have no NLB is: ' + str(len(allImages)-len(uniquelist)))

    return uniquelist

def copyRowsofImagesWithNoNLBToNewCSV():
    print(boomAnnotations.head)
    df_filtered = boomAnnotations[(boomAnnotations['xmin'] != 0) & (boomAnnotations['ymin'] != 0) & (boomAnnotations['xmax'] != 0) & (boomAnnotations['ymax'] != 0)]
    print(df_filtered.head)
    df_filtered.to_csv('annotations_boom_edit.csv', index=False)

def deleteImagesWithNoNLB():
    nlbimages = []
    for image in uniqueNamesofNoneNLBImagesList:
        imageName=image
        shutil.move(imageName, 'nonNLBImages/'+imageName)
        #os.remove(imageName)
    for file in glob.glob("*.JPG"):
        nlbimages.append(file)
    print('Total number of images after deleting none  NLB images is: ' + str(len(nlbimages)))
#function calls
getNamesofAllImagesInBoomFolder()
uniqueNamesofNoneNLBImagesList=getNamesOfAllNoneNLBImages()
#copyRowsofImagesWithNoNLBToNewCSV()
deleteImagesWithNoNLB()
#print(allImages)




#editedBoomAnnotations = pd.read_csv('annotations_boom_edit.csv')
#print('Number of rows in the new edited annotaions file is:'+ str(len(editedBoomAnnotations)))

