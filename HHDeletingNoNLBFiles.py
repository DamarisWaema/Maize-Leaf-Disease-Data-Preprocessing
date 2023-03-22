import glob, os
import pandas as pd
import csv
import shutil
#Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np
os.chdir("D:/PHD Data/Real NBL/images_handheld")
handHeldAnnotationsEdit1 = pd.read_csv('annotations_handheld_edit1.csv')

allImages=[]
allNoneNLBImages=[]
uniqueNamesofNoneNLBImagesList=[]


def getNamesofAllImagesInHandHeldFolder():
    for file in glob.glob("*.JPG"):
        allImages.append(file)

    for file in glob.glob("*.Jpeg"):
        allImages.append(file)
    print('Total number of images before deleting none NLB ones is: ' + str(len(allImages)))
#Looking into the data to find out number of images that have no NLB
def getNamesOfAllNoneNLBImages():
    for _, row in handHeldAnnotationsEdit1.iterrows():
        if row.x1 == 0 and row.y1 ==0 and row.x2 == 0 and row.y2 ==0:
            image_Name=row.filename
            allNoneNLBImages.append(image_Name)
    # converting list to set to get unique names/remove duplicates
    uniqueNamesofNoneNLBImagesSet = set(allNoneNLBImages)
    uniquelist=list(uniqueNamesofNoneNLBImagesSet)
    print('Total number of annotation rows for all data is: ' +str(len(handHeldAnnotationsEdit1)))

    print('Total number of rows that have no NLB is: ' + str(len(allNoneNLBImages)))
    print('Total number of images that have no NLB is: ' + str(len(uniquelist)))
    print('Total number of images that have NLB is: ' + str(len(allImages)-len(uniquelist)))

    return uniquelist

def copyRowsofImagesWithNLBToNewCSV():
    print(handHeldAnnotationsEdit1.head)
    df_filtered = handHeldAnnotationsEdit1[(handHeldAnnotationsEdit1['x1'] != 0) & (handHeldAnnotationsEdit1['y1'] != 0) & (handHeldAnnotationsEdit1['x2'] != 0) & (handHeldAnnotationsEdit1['y2'] != 0)]
    print(df_filtered.head)
    print('Total number of annotation rows for all data is: ' +str(len(handHeldAnnotationsEdit1)))
    print('Total number of annotation rows for only images with NLB is: : ' +str(len(df_filtered)))

    df_filtered.to_csv('annotations_handheld_edit2.csv', index=False)

def deleteImagesWithNoNLB():
    nlbimages = []
    for image in uniqueNamesofNoneNLBImagesList:
        imageName=image
        shutil.move(imageName, 'nonNLBImages/'+imageName)
        #os.remove(imageName)
    for file in glob.glob("*.JPG"):
        nlbimages.append(file)
    for file in glob.glob("*.Jpeg"):
        nlbimages.append(file)
    print('Total number of images after deleting none  NLB images is: ' + str(len(nlbimages)))

#function calls
#getNamesofAllImagesInHandHeldFolder()
#uniqueNamesofNoneNLBImagesList=getNamesOfAllNoneNLBImages()
#copyRowsofImagesWithNLBToNewCSV()
#deleteImagesWithNoNLB()
#print(allImages)




#editedBoomAnnotations = pd.read_csv('annotations_boom_edit.csv')
#print('Number of rows in the new edited annotaions file is:'+ str(len(editedBoomAnnotations)))