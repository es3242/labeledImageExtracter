import os
from PIL import Image
import xml.etree.ElementTree as ET

#라벨링 된 바운딩 박스 내 이미지 crop

def makeDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def makeObjectsDir(base):
    makeDirectory(base+"/Objects")


def cropObjects(base):
    imgPath = base+"/JPEGImages/"
    labelPath = base+"/Annotations/"
    file_list = os.listdir(imgPath)
    file_list_jpg = [file for file in file_list if file.endswith(".jpg")]
    ImageCnt=len(file_list_jpg)
    makeObjectsDir(base)
    j=0

    for file in file_list_jpg:
        j+=1
        if j % int(ImageCnt*0.01) == 0:
            print(f"{j // int(ImageCnt*0.01)}%")
        img = Image.open(imgPath+file)
        xml = open(labelPath+file[:-4]+".xml", "r")

        tree = ET.parse(xml)
        root = tree.getroot()
        objects = root.findall("object")
        
        i=0
        for _object in objects:
            i += 1
            name = _object.find("name").text
            makeDirectory(base+"/Objects/"+name)
        

            bndbox = _object.find("bndbox")
            xmin = float(bndbox.find("xmin").text)
            ymin = float(bndbox.find("ymin").text)
            xmax = float(bndbox.find("xmax").text)
            ymax = float(bndbox.find("ymax").text)

            cropped = img.crop((xmin, ymin, xmax, ymax))
            cropped.save(f'{base}/Objects/{name}/{file[:-4]}_{i}.png')

#cropObjects(dir)



