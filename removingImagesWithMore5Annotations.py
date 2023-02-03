import glob, os
import shutil
import pandas as pd
from PIL import Image

os.chdir("D:/PHD Data/Real NBL/images_boom")
allImages=[]
imagesGreaterthan5Annotations=[]
boomAnnotationsEdit2 = pd.read_csv('annotations_boom_edit2.csv')



