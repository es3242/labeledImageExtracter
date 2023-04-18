import shutil
import os


# imgPath 밑에 /samples 디렉터리를 만든 후 
# imgPath 내 이미지 파일 n개 중 SAMPLE_NUM 수 만큼 이미지를 뽑아 
# /samples내로 옮김

SAMPLE_NUM = 1000

def makeDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def getSampleImages(imgPath):
    makeDirectory(imgPath + "/samples")
    samplePath = imgPath + "/samples"

    src = imgPath+'/'
    dir = samplePath+'/'

    file_list = os.listdir(imgPath)
    file_list_jpg = [file for file in file_list if file.endswith(".png")]
    ImageCnt=len(file_list_jpg)

    n = ImageCnt//SAMPLE_NUM

    for i in range(SAMPLE_NUM):
        filename = file_list_jpg[i*n]
        shutil.move(src + filename, dir + filename)

#getSampleImages(imgPath)