import glob, os
import shutil
import pandas as pd
from PIL import Image

os.chdir("D:/PHD Data/Real NBL/images_boom")
allImages=[]
sampledImages=[]
boomAnnotationsEdit3 = pd.read_csv('annotations_boom_edit3.csv')
dummyImages=[]
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

    x=0
    totalNumberImages=len(allImages)
    while x<=totalNumberImages:
        for image in allImages:


getNamesofAllImagesInBoomFolder()
#testingSampling
sample500Images()