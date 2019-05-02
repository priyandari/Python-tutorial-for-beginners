# FIleReadWrite.py
# Kumpulan fungsi untuk Read/Write

import os

def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()

def readFile(filePath):
    if not fileExists(filePath):
        print('File, ' + filePath + ' tidak ada - tidak dapat dibaca. ')
        return ''
    
    fileHandle = open(filePath, 'r')
    data = fileHandle.read()
    fileHandle.close()
    return data


