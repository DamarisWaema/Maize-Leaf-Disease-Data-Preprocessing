import glob, os
import shutil
import pandas as pd
from PIL import Image

os.chdir("D:/PHD Data/Real NBL/images_boom")
allImages=[]
sampledImages=[]
boomAnnotationsEdit3 = pd.read_csv('annotations_boom_edit3.csv')
dummyImages=[]
#unsampledImagesToDelete=[]
def getNamesofAllImagesInBoomFolder():
    for file in glob.glob("*.JPG"):
        image_Name = file.split(".")
        image_Name = image_Name[0]
        allImages.append(image_Name)
    print('Total number of images before sampling is: ' + str(len(allImages)))
def testingSampling():
  x=0
  y=2936
  while x<=y:
    if x%6==0:
        dummyImages.append(x)
    x+=1
  print(len(dummyImages))
  print(x)

def sample500Images():

    for image in allImages:
        if allImages.index(image)%6==0:
            sampledImages.append(image)

    print('Total number of sampled images is: '+str(len(sampledImages)))
    unsampled=list(set(allImages)-set(sampledImages))
    print('Total number of unsampled images to be deleted is: ' +str(len(unsampled)))
    return unsampled
def removeunsampledImagesAnnotationsFromCSV3():
    df_filtered = boomAnnotationsEdit3
    annotaionsfor2936B4Sampling=len(df_filtered)
    for image_Name in unsampledImagesToDelete:
        for _, row in df_filtered.iterrows():
            if row.imageName == image_Name:
                df_filtered = df_filtered[(df_filtered['imageName'] != image_Name)]
    #print(df_filtered.head)
    print('Total number of annotations for the 2936 images before sampling is: '+ str(annotaionsfor2936B4Sampling))
    print('Total number of annotations for the 490 sampled images is: '+ str(len(df_filtered)))
    print('Total number of annotations for the 2446 removed after sampling is: '+ str(annotaionsfor2936B4Sampling-len(df_filtered)))

    df_filtered.to_csv('annotations_boom_edit4.csv', index=False)

def moveUnsampledImages():
    for image in unsampledImagesToDelete:
        name = image + '.JPG'
        shutil.move(name, '2446UnsampledImages/' + name)

getNamesofAllImagesInBoomFolder()
#testingSampling
unsampledImagesToDelete=sample500Images()
#removeunsampledImagesAnnotationsFromCSV3()
moveUnsampledImages()