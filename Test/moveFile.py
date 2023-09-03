import os
import shutil

copyDir = 'D:\\Project\\Road Motorcycle Helmet Detection\\VOCdevkit\\VOC2007\\YOLOLables'

putDir = 'D:\\Temp\\temp\\'

for root, dirs, files in os.walk(copyDir):
    for fileName in files:
        fileName = fileName.replace('.txt', '')
        if int(fileName) % 2 == 0 or (int(fileName) >= 0 and int(fileName) <= 500 ):
            fileP = root + '/' + fileName + '.txt'
            
            newFP = putDir + '/' + fileName + '.txt'
            
            shutil.copyfile(fileP, newFP)
            
            print(fileName + ' finish')