import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import argparse

def userChoice(nameOfVideo, kindOfGas) :
    video_object = cv2.VideoCapture("C:\\Users\\קרן\\Documents\\Hackatal\\"+nameOfVideo+".mp4")

    if nameOfVideo=="videoplayback":
        xs = [60, 150]
        ys = [68, 250]
    if nameOfVideo=="videoplayback (2)":
        xs = [110, 200]
        ys = [126, 300]



    success = True
    i=1
    flagGreen=0
    flagOrange=0
    globalFlag=0
    while success:
        success,frame = video_object.read()
        #plt.imshow(frame)
        #img = Image.open('frame').convert('LA')
        #img.save('greyscale.png')
        if success:
            
            #mpimg.imsave(r"C:/Users/קרן/Documents/Hackatal/TEST/img"+"_"+str(i)+".jpg",frame)
            #img=mpimg.imread(r"C:/Users/קרן/Documents/Hackatal/img"+"_"+str(i)+".jpg")
            # load the image
            cropped_frame=frame[ys[0]:ys[1], xs[0]:xs[1]]
            image=cropped_frame
            #if i==1:
            #   plt.imshow(image)
            if globalFlag==0 :
                Orange_MIN = np.array([60, 20, 0], np.uint8)
                Orange_MAX = np.array([120, 60, 10], np.uint8)
                dstOrange = cv2.inRange(image, Orange_MIN, Orange_MAX)
                orangeOutput = cv2.bitwise_and(image, image, mask = dstOrange)
                no_orange = cv2.countNonZero(dstOrange)
                #print(no_orange)
                if no_orange==0 :
                    flagOrange=1
                    globalFlag=1
                    #cv2.namedWindow("opencv")
                    #plt.imshow(np.hstack([image, orangeOutput]))
            
                Green_MIN = np.array([30, 40, 10], np.uint8)
                Green_MAX = np.array([60, 85, 30], np.uint8)
                dstGreen = cv2.inRange(image, Green_MIN, Green_MAX)
                greenOutput = cv2.bitwise_and(image, image, mask = dstGreen)
                no_green = cv2.countNonZero(dstGreen)
                #_print(no_green)
                if no_green==0 :
                    flagGreen=1
                    globalFlag=1
                    #onlyColorsOutput=orangeOutput+greenOutput
                    #plt.imshow(onlyColorsOutput)
                
                if flagGreen==1 : #95
                    if kindOfGas=='95':
                        return 1
                    else:
                        return 0
                if flagOrange==1 : #SOLAR
                    if kindOfGas=='SOLAR':
                        return 1
                    else:
                        return 0
            #cv2.namedWindow("opencv")
            #plt.imshow(np.hstack([image, greenOutput]))
        #else :
            #if globalFlag==0 :
                #print(refImg[ys[0], xs[0]])
                #cropped_frame=frame[ys[0]:ys[1], xs[0]:xs[1]]
                #mpimg.imsave(r"C:/Users/קרן/Documents/Hackatal/cropped_frame.jpg",cropped_frame)
                #print(i)
                #print(cropped_frame)
                #if i==2:
                    #plt.imshow(cropped_frame)
        
            i=i+1
            
