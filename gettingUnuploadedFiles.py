import glob, os
import pandas as pd
import cv2

import csv
import shutil
# Convootls package is used to enable deleting rows from the CSV for images without NLB
from convtools import conversion as c
from convtools.contrib.tables import Table
import numpy as np

os.chdir("D:/Image Preprocessing Matlab/testing/trainCV2NormalizedMaxpooled")
annotationsAll = pd.read_csv('annotationsTrain-CV2Norm-MP.csv')
uploaded=pd.read_csv('aaploadedImages.csv')
# toUpload=pd.read_csv('appload.csv')
availableImages=[]
allImages=[]
images=[]
def getUnuploadedImages():

    available=uploaded.filename.unique()
    for name in available:
        availableImages.append(name)
    toUpload=set(annotationsAll.filename.unique())-set(availableImages)

   # df = pd.DataFrame(toUpload)
    print(len(toUpload))
    # print(df.head())
    #df.to_csv('appload.csv', index=False)
    #print(len(toUpload))
    return list(toUpload)
def copyImages():
    #images=toUpload.filename.unique()

    for image in images:
        # name = image.split('.jpg')
        # newName=name[0]+ '-CQ32.jpg'
        shutil.copy(image, 'toUpload/' + image)

# def colorQuant(Z, K, criteria, img):
#     ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
#
#     # Now convert back into uint8, and make original image
#     center = np.uint8(center)
#     res = center[label.flatten()]
#     res2 = res.reshape((img.shape))
#     return res2
# def CQ32():
#     for image in images:
#         img = cv2.imread(image)
#         Z = img.reshape((-1, 3))
#
#         # convert to np.float32
#         Z = np.float32(Z)
#
#         # define criteria, number of clusters(K) and apply kmeans()
#         criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#         CQImg = colorQuant(Z, 64, criteria, img)
#         name = image.split('.')
#
#         fullname = name[0] + '-CQ64.jpg'
#         #print(fullname)
#         cv2.imwrite('CQ64/' + fullname, CQImg)
# #
# def checkingIfNamesMatch():
#     for file in glob.glob("*.jpg"):
#         allImages.append(file)
#     print('Total number of images before deleting none NLB ones is: ' + str(len(allImages)))
#     names=annotationsAll.filename.unique()
#     difference=set(allImages)-set(names)
#     print(difference)
images=getUnuploadedImages()
#CQ32()
copyImages()
# checkingIfNamesMatch()