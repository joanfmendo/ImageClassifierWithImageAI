import cv2

### Function to resize an image based on a proportion
def ProportionalResize(filepath,scale_percent):
    img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    width = int(img.shape[1] * scale_percent)
    height = int(img.shape[0] * scale_percent)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

### Function to resize an image based on a given dimension
def CustomResize(filepath,width, height):
    dim = (width, height)
    img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

### Function to resize an image based on is width
def WidthBasedResize(filepath,width):
    img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    height = int(img.shape[0] * (width/img.shape[1]))
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

### Function to resize an image based on is width
def HeightBasedResize(filepath,height):
    img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    width = int(img.shape[1] * (height/img.shape[0]))
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

filepath = 'original images/sexy_cop_bw.jpg'
'''
scale_percent = 0.2
resized = ProportionalResize(filepath,scale_percent)
cv2.imwrite("proportional.png", resized)

width = 200
height = 200
resized = CustomResize(filepath,width, height)
cv2.imwrite("custom.png", resized)

width = 300
resized = WidthBasedResize(filepath,width)
cv2.imwrite("widthbased.png", resized)

height = 400
resized = HeightBasedResize(filepath,height)
cv2.imwrite("heightbased.png", resized)
'''

from os import listdir
from os.path import isfile, join
import os

os.getcwd()

#ofp = 'I:/Ejemplos Fotografía/Retratos & Moda/Lingerie/' #Original Files Path
ofp = 'original images/' #Original Files Path
rfp = 'resized images/' #Resized Files Path
files = [f for f in listdir(ofp) if isfile(join(ofp, f))]

width = 200
height = 200
for file in files:
    print(file)
    resized = CustomResize(str(ofp+file), width, height)
    cv2.imwrite(str(rfp+'resized_'+file), resized)
