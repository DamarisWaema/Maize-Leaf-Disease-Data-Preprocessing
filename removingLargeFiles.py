import glob, os
import shutil
import pandas as pd

os.chdir("D:/PHD Data/Real NBL/images_boom")
allImages=[]
images_40006000=[]
from PIL import Image


# img = Image.open('DSC00965_0.JPG')
#
# # get width and height
# width = img.width
# height = img.height
#
# # display width and height
# print("The height of the image is: ", height)
# print("The width of the image is: ", width)


#Getting Names of All images in the boom folder
def getNamesofAllImagesInBoomFolder():
    for file in glob.glob("*.JPG"):
        allImages.append(file)
    print('Total number of images before deleting 6000*4000 or 4000*6000 ones is: ' + str(len(allImages)))

def count6000_4000AND4000_6000Images():
    for file in glob.glob("*.JPG"):
        img = Image.open(file)
        if (img.width==4000 and img.height==6000 ) or (img.width==6000 and img.height==4000):
            images_40006000.append(file)
    print('Total number of images that are 6000*4000 or 4000*6000 is: ' + str(len(images_40006000)))
    print('Total number of images to remain after deleting 6000*4000 or 4000*6000 ones is: ' + str(len(allImages)-len(images_40006000)))

def move6000_4000AND4000_6000Images():
    for image in images_40006000:
        imageName=image
        shutil.move(imageName, 'images_4000_6000/'+imageName)

def remove6000_4000AND4000_6000ImagesAnnotationsFromCSV():
    largeImages=[]
    boomAnnotationsEdit1 = pd.read_csv('annotations_boom_edit1.csv')
    df_filtered=boomAnnotationsEdit1
    print(boomAnnotationsEdit1.head)
    for file in glob.glob("images_4000_6000/*.JPG"):
        largeImages.append(file)
    print('Total number of images before deleting 6000*4000 or 4000*6000 ones is: ' + str(len(largeImages)))


    for image in largeImages:
        tempTuple = os.path.splitext(image)
        image_Name = tempTuple[0]
        image_Name = image_Name.split("\\")
        image_Name = image_Name[1]
        for _, row in df_filtered.iterrows():
            if row.imageName == image_Name:
                df_filtered = df_filtered[(df_filtered['imageName'] != image_Name)]
    print(df_filtered.head)
    df_filtered.to_csv('annotations_boom_edit2.csv', index=False)


#getNamesofAllImagesInBoomFolder() #gets all images before deleting 6000*4000 or 4000*6000 ones
#count6000_4000AND4000_6000Images() #moves all images that are 6000*4000 or 4000*6000 to a different folder
#move6000_4000AND4000_6000Images()
#remove6000_4000AND4000_6000ImagesAnnotationsFromCSV()