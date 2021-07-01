import warnings
warnings.filterwarnings('ignore')

import cv2
vidcap = cv2.VideoCapture("The Office (US) 6x01 - Gossip.mp4")
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("Images/image"+str(count)+".jpg", image)     # save frame as a JPG file
    return hasFrames
sec = 0
frameRate = 1
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

from mtcnn import MTCNN
import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
def crop_image(image_path):         #crops out the face (extracts the face)
    detector = MTCNN() 
    img=cv2.imread(image_path)
    data=detector.detect_faces(img)
    biggest=0
    if data !=[]:
        for faces in data:
            box=faces['box']            
            # calculate the area in the image
            area = box[3]  * box[2]
            if area>biggest:
                biggest=area
                bbox=box 
        bbox[0]= 0 if bbox[0]<0 else bbox[0]
        bbox[1]= 0 if bbox[1]<0 else bbox[1]
        img=img[bbox[1]: bbox[1]+bbox[3],bbox[0]: bbox[0]+ bbox[2]] 
        return img
    else:
        return (False, None)

import os
# assign directory
directory = 'Images/'
# iterate over files in that directory
c=0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    try:
        c=c+1
        img=crop_image(f)
        cv2.imwrite('FaceExtracts/face'+str(c)+'.jpg', img)
    except:
        continue
