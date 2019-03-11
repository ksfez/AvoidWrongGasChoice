import requests
import base64
import json
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import argparse
# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
def identifyPlate(nameOfVideo):
  
    video_object = cv2.VideoCapture("C:\\Users\\קרן\\Documents\\Hackatal\\"+nameOfVideo+".mp4")
    success = True
    response = 0
    while success and response==0 :
        success,frame = video_object.read()
        if success:
            plt.imsave("car.jpg",frame)
            IMAGE_PATH = 'car.jpg'
            SECRET_KEY = 'sk_eecd4b9957b2775cf16309e4'
            with open(IMAGE_PATH, 'rb') as image_file:
                img_base64 = base64.b64encode(image_file.read())

            url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=eu&secret_key=%s' % (SECRET_KEY)

            r = requests.post(url, data = img_base64)
    
            result=json.dumps(r.json(), indent=2)
    
            resp = json.loads(result)
    
            if resp['results']==[]:
                response=0
            else :
                response=resp['results'][0]['plate']
        
    return response

