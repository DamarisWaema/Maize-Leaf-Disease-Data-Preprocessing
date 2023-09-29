# import Opencv
import cv2
import shutil
# import Numpy
#import numpy as np
import numpy as ppool

import glob, os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir("D:/PHD Data/Real NBL/final641HHTestImages-2-MaxPooling1")
for file in glob.glob("*.jpg"):

    img = cv2.imread(file)
    norm = ppool.zeros((800,800))
    final = cv2.normalize(img,  norm, 0, 255, cv2.NORM_MINMAX)
    name=file.split('-MaxPooling.jpg')

    fullname=name[0]+'-CV2Normalized.jpg'
    cv2.imwrite('CV2Normalized/'+fullname, final)

# for file in glob.glob("*-CV2Normalized.jpg"):
#     shutil.move(file, 'train-CV2Normalized/'+file)
#     #os.remove(file)
