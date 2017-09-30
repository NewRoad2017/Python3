# -*- coding: utf-8 -*-
import os
#conbine the fileDir with the fileName
def CombinePathpurely(dataDir,dataName):
    return dataDir+"/"+dataName

def CombinefilePath(datafileDir, datafileName, dataExtension):
    filePath = datafileDir + "/" + datafileName
    if os.path.isdir(filePath):
        pass
    else:
        fileNameParts = os.path.splitext(datafileName)
        if fileNameParts[1] != '':
            pass
        else:
            filePath = datafileDir + "/" + datafileName + dataExtension
    #filePath = filePath.decode('utf-8')
    return filePath

def SplitFileName(dataFilename):
    listParts = os.path.splitext(dataFilename)
    return listParts[0],listParts[1]

def JudgeFile(dataFilePath):
    if os.path.isfile(dataFilePath):
        return True
    else:
        return False

def GetFileSize(dataPath):
    fileSize = os.path.getsize(dataPath)/1024
    return fileSize


