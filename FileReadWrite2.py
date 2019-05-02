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

# Tambahan fungsi untuk membaca dan menulis file pada baris tertentu
def openFileforWrite(filePath):
    fileHandle = open(filePath, 'w')
    return fileHandle

def writeALine(fileHandle, lineToWrite):
    lineToWrite = lineToWrite + '\n'
    fileHandle.write(lineToWrite)

def openFileforRead(filePath):
    if not fileExists(filePath):
        print('File ' + filePath + ' tidak ada')
        return ''
    else:
        fileHandle = open(filePath, 'r')
        return fileHandle

def readALine(fileHandle):
    baris = fileHandle.readline()

    # Bagian ini berfungsi memeriksa bagian akhir file (EOF)
    # Jika tidak ada baris lagi, mengembalikan nilai False
    if not baris:
        return False

    # Jika baris berakhir dengan character '\n', tandai sebagai akhir baris
    if baris.endswith('\n'):
        baris = baris.rstrip('\n')

    return baris

def closeFile(fileHandle):
    fileHandle.close()