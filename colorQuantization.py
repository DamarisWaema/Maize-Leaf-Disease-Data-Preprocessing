import glob, os
import pandas as pd
import cv2

import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/PHD Data/Real NBL/final641HHTestImages-2")
annotationsAll = pd.read_csv('annotationsTest-2.csv')

availableImages=[]

def colorQuant(Z, K, criteria, img):
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return res2
def CQ32():
    images=annotationsAll.filename.unique()
    for image in images:
        img = cv2.imread(image)
        Z = img.reshape((-1, 3))

        # convert to np.float32
        Z = np.float32(Z)

        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        CQImg = colorQuant(Z, 32, criteria, img)
        name = image.split('.')

        fullname = name[0] + '-CQ32-20.jpg'
        #print(fullname)
        cv2.imwrite('CQ32-20Iterations/' + fullname, CQImg)

CQ32()
