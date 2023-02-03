import glob, os
import shutil
import pandas as pd
from PIL import Image

os.chdir("D:/PHD Data/Real NBL/images_boom")
allImages=[]
images5OrMoreAnnotations=[]
boomAnnotationsEdit2 = pd.read_csv('annotations_boom_edit2.csv')


def getNamesofAllImagesInBoomFolder():
    for file in glob.glob("*.JPG"):
        image_Name = file.split(".")
        image_Name = image_Name[0]
        allImages.append(image_Name)
    print('Total number of images before deleting >=5 annotations ones is: ' + str(len(allImages)))
def getNamesOf5OrMoreAnnotationsImages():
    annotationsFor5OrMoreAnnotationsImages = 0
    for image_Name in allImages:
        annotaions=  len(boomAnnotationsEdit2[boomAnnotationsEdit2["imageName"]==image_Name])

        if annotaions>=5:
            annotationsFor5OrMoreAnnotationsImages=annotationsFor5OrMoreAnnotationsImages+annotaions
            images5OrMoreAnnotations.append(image_Name)
    print('Total number of images with >=5 annotations is: ' + str(len(images5OrMoreAnnotations)))
    print('Images to be left after deleting those with 5 or more annotations is: '+ str(len(allImages)-len(images5OrMoreAnnotations)))
    print('Total number of annotations for images with 5 or more annotations is: '+str(annotationsFor5OrMoreAnnotationsImages))
    print('Total number of annotations to remain after deleting those for images with 5 or more annotations is: ' +str(len(boomAnnotationsEdit2)-annotationsFor5OrMoreAnnotationsImages))
    #print('First image with 5 or more annotations is: ' +images5OrMoreAnnotations[0])
    #annotationsNumber=len(boomAnnotationsEdit2[boomAnnotationsEdit2["imageName"]==images5OrMoreAnnotations[0]])
    #print('That image has this number of annotations: ' +str(annotationsNumber))

def moveImageswith5OrMoreAnnotations():
    for image_Name in images5OrMoreAnnotations:
        name=image_Name+'.JPG'
        shutil.move(name, 'images5OrMoreAnnotations/' + name)

def deleteAnnotationsForImagesWith5OrMoreAnnotations():
    manyAnnotationsImages=[]
    df_filtered = boomAnnotationsEdit2
    for file in glob.glob("images5OrMoreAnnotations/*.JPG"):
        tempTuple = os.path.splitext(file)
        image_Name = tempTuple[0]
        image_Name = image_Name.split("\\")
        image_Name = image_Name[1]
        manyAnnotationsImages.append(image_Name)
    print(manyAnnotationsImages[0])
    for image_Name in manyAnnotationsImages:
        for _, row in df_filtered.iterrows():
            if row.imageName == image_Name:
                df_filtered = df_filtered[(df_filtered['imageName'] != image_Name)]
    print(df_filtered.head)
    df_filtered.to_csv('annotations_boom_edit3.csv', index=False)


#getNamesofAllImagesInBoomFolder()
#getNamesOf5OrMoreAnnotationsImages()
#moveImageswith5OrMoreAnnotations()
#deleteAnnotationsForImagesWith5OrMoreAnnotations()