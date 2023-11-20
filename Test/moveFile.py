import os
import shutil

copyDir = 'D:\Project\Road Motorcycle Helmet Detection\VOCdevkit\VOC2007\JPEGImages'

putDir = 'D:\\Project\\Road Motorcycle Helmet Detection\\VOCdevkit\\images\\val'

dictionary = ['.txt', '.jpg']
direction = dictionary[1]

for root, dirs, files in os.walk(copyDir):
    for fileName in files:
        fileName = fileName.replace(direction, '')
        fileP = root + '/' + fileName + direction
        if int(fileName) % 2 == 0 and (int(fileName) >= 0 and int(fileName) <= 500 ):
            newFP = putDir + '/' + fileName + direction
            
            shutil.copyfile(fileP, newFP)
            
            print(fileName + ' finish')