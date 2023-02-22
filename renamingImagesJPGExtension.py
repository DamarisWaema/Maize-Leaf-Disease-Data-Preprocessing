import glob, os
import shutil

import pandas as pd
from PIL import Image
from numpy import random
from random import choice

os.chdir("D:/PHD Data/Real NBL/images_boom")
boomAnnotationsEdit5 = pd.read_csv('annotations_boom_edit5.csv')
boomAnnotationsEdit6 = pd.read_csv('annotations_boom_edit6.csv')

def renameImagesJPG():

    for _, row in boomAnnotationsEdit5.iterrows():
        newImageName=row.image_name+'.JPG'
        boomAnnotationsEdit5['image_name'] = boomAnnotationsEdit5['image_name'].replace([row.image_name], newImageName)
    #print(boomAnnotationsEdit5.head)
    boomAnnotationsEdit5.to_csv('annotations_boom_edit7.csv', index=False)

def renameTestImagesJPG():
    for _, row in boomAnnotationsEdit6.iterrows():
        newImageName=row.image_name+'.JPG'
        boomAnnotationsEdit6['image_name'] = boomAnnotationsEdit6['image_name'].replace([row.image_name], newImageName)
    print(boomAnnotationsEdit6.head)
    boomAnnotationsEdit6.to_csv('annotations_boom_edit8.csv', index=False)

#renameImagesJPG() # renames image names in annotations_boom_edit5.csv
#renameTestImagesJPG()