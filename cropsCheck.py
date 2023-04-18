import os
from PIL import Image
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import sys 
import cv2

#라벨링 된 사진들 검수용. 미완성

def deleteImage(orgImg):
    os.remove(orgImg)
    print('Image deleted')

def checkOutput(path):
    file_list = os.listdir(path)
    file_list_jpg = [file for file in file_list if file.endswith(".png")]

    for file in file_list_jpg:
        orgImg = Image.open(path+'/'+file)
        x = orgImg.size[0]
        y = orgImg.size[1]
        newSize = (x*20,y*20)

        orgImg.show(orgImg.resize(newSize))

        while(True):
            key = str(input("condtinue: c, deltete: d,exit: x \n"))

            if key == 'c':
                
                break
            if key == 'd':
                deleteImage(orgImg)
                break

            if key == 'x':
                print(orgImg)
                sys.exit("exit.") 


            else: continue
