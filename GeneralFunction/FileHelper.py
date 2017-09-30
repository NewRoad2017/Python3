# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('D:/Applications/Python3/GeneralFunction')
from GeneralFunction import *
from shutil import copy
import threading
import time,random

def GetTheFirsrFolders(dataDir, listProcesses):
    listFolders = []
    listFolders.append(dataDir)
    listFiles = GetDirfiles(dataDir)
    for index in range(0, len(listFiles)):
        fileName = listFiles[index]
        filePath = PathHelper.CombinePathpurely(dataDir, fileName)
        print(filePath)
        if os.path.isfile(filePath):
            pass
        else:
            print(filePath + "is a folder")
            ExtractFolders(filePath, listFolders)
    return listFolders

def ExtractFolders(dataDir, listFolders):
    listFolders.append(dataDir)
    listFiles = GetDirfiles(dataDir)
    for index in range(0,len(listFiles)):
        fileName = listFiles[index]
        filePath = PathHelper.CombinePathpurely(dataDir,fileName)
        print(filePath)
        if os.path.isfile(filePath):
            pass
        else:
            print(filePath + "is a folder")

            ExtractFolders(filePath, listFolders)
    return listFolders


##
#establish the folder
def MakeDir(dataDir):
    os.mkdir(dataDir)

## to move file
# to move the file to another place
def MoveFile(dataOriPath, dataTarPath):
    copy(dataOriPath, dataTarPath)
    os.remove(dataOriPath)
    strDir = os.path.dirname(dataTarPath)
    print ("move "+dataOriPath + " into "+ strDir)

## to dulplicate file
# to dulplicate the file to another place
def DulplicateFile(dataOriPath,dataTarPath):
    copy(dataOriPath,dataTarPath)
    tarPathparts = os.path.split(dataTarPath)
    print ("copy "+dataOriPath + " into "+tarPathparts[1])

#extract all the files with ".docx" and ".doc" in this dir to another file dir
def MergeFiles(dataOriDir, dataTarDir, dataExtensions,index):
    listFiles = GetDirfiles(dataOriDir)
    for fileCurrent in listFiles:
        oriDir = PathHelper.CombinePathpurely(dataOriDir, fileCurrent)
        if os.path.isfile(oriDir):
            listFileParts = os.path.splitext(fileCurrent)
            # if listFileParts[1] == dataExtensions:
            #     tarFilePath = PathHelper.CombinefilePath(dataTarDir, str(index), dataExtensions)
            #     DulplicateFile(oriDir, tarFilePath)
            #     index = index+1
            for extension in dataExtensions:
                if listFileParts[1] == extension:
                    tarFilePath = PathHelper.CombinefilePath(dataTarDir,str(index),extension)
                    DulplicateFile(oriDir, tarFilePath)
                    index = index+1
                    break
        else:
            print ("to go into" + oriDir + str(index))
            index = MergeFiles(oriDir, dataTarDir,dataExtensions,index)
            print ("out" + oriDir + str(index))
    return index


def Extractfiles1(dataOriDir, dataTarDir, dataLog, dataExtensions =None, datafSizes = None):
    dataLog.PrepareWrite('Origin Path:%s ' % (dataOriDir))
    index = 0
    for fileDir, listFolders, listFiles in os.walk(dataOriDir):
        dataLog.PrepareWrite('Path Direction:%s ' % (fileDir))
        for fileName in listFiles:
            filePath = PathHelper.CombinePathpurely(fileDir, fileName)
            fileNameOnly,fileExtension = PathHelper.SplitFileName(fileName)
            if dataExtensions is not None:
                status = 0
                dataExtensions = list(dataExtensions)
                for extension in dataExtensions:
                    if fileExtension == extension:
                        status = 1
                        dataLog.PrepareWrite('    %s,file: %s' % (extension, fileName))
                        break
                if not status:
                    continue
            #file size
            if datafSizes is not None:
                datafSizes = list(datafSizes)
                fileSize = PathHelper.GetFileSize(filePath)
                if fileSize < datafSizes[1] and fileSize > datafSizes[0]:
                    dataLog.PrepareWrite('%s,file: %s' % (str(fileSize), fileName))
                    tarFilePath = PathHelper.CombinefilePath(dataTarDir, fileNameOnly + '_' + str(index), extension)
                    DulplicateFile(filePath, tarFilePath)
                    index = index + 1
    dataLog.PrepareWrite('the file count is %s' % (str(len(os.listdir(dataTarDir)))))




def Extractfiles(dataOriDir, dataTarDir, dataExtensions,dataLog,dataListThreads):
    dataLog.PrepareWrite("RUNING %s,the path is %s" % (threading.current_thread().name,dataOriDir))
    listFiles = [file for file in os.listdir(dataOriDir)]
    for fileName in listFiles:
        filePath = PathHelper.CombinePathpurely(dataOriDir, fileName)
        if os.path.isfile(filePath):
            listFileParts = os.path.splitext(fileName)
            for extension in dataExtensions:
                if listFileParts[1] == extension:
                    print('    %s,file: %s' % (threading.current_thread().name, fileName))
                    tarFilePath = PathHelper.CombinefilePath(dataTarDir,threading.current_thread().name + "_"+fileName,extension)
                    DulplicateFile(filePath, tarFilePath)
                    break
        else:
            dataLog.PrepareWrite("%s ASSIGN:for %s is assigned" % (threading.current_thread().name,filePath))
            thread = threading.Thread(target=continueGo,args=(filePath,dataTarDir, dataExtensions,dataLog,dataListThreads,))
            dataListThreads.append(thread)
            thread.start()
    # print(threading.current_thread().is_alive())
    dataLog.PrepareWrite("END %s ,the path is %s" % (threading.current_thread().name,dataOriDir))


def continueGo(dataOriDir,dataTarDir,dataExtensions,dataLog,dataListThreads):
    Extractfiles(dataOriDir, dataTarDir, dataExtensions,dataLog,dataListThreads)


def DeleteFiles(dataFileDir,dataFileNames,dataExtension):
    for index in range(0,len(dataFileNames)):
        fileCurrent = dataFileNames[index]
        #fileCurrent = dataFileNames[index].decode("utf-8")
        filePath = PathHelper.CombinefilePath(dataFileDir, fileCurrent, dataExtension)
        os.remove(filePath)
        print ("Delete File: "+ filePath)

def GetDirfiles(dataFileDir):
    return  os.listdir(dataFileDir)


def RenameFile(dataFileDir,dataFilenameOri,dataFilenameLast):
    filePathOri = PathHelper.CombinePathpurely(dataFileDir, dataFilenameOri)
    filePathLast = PathHelper.CombinePathpurely(dataFileDir, dataFilenameLast)
    os.rename(filePathOri,filePathLast)


def BatchRenamefiles(dataFileDir,dataBatch):
    listFiles = GetDirfiles(dataFileDir)
    filesCount = len(listFiles)
    for index in range(0,filesCount):
        fileName= listFiles[index]
        fileNameLast = dataBatch["batchName"]+str(index)+dataBatch["batchEx"]
        RenameFile(dataFileDir,fileName,fileNameLast)

##
#the series of folder operations
def BatchCreatFolders(dataDir, dataCount, dataBeginnumber, dataInerterval, dataBatchName):
    for index in range(dataBeginnumber,dataBeginnumber+dataCount*dataInerterval):
        folderName = dataBatchName+str(index)
        folderPath = PathHelper.CombinePathpurely(dataDir, folderName)
        if os.path.exists(folderPath):
            pass
        else:
            os.mkdir(folderPath)

def ExtractFolders(dataDir, listFolders):
    listFolders.append(dataDir)
    listFiles = FileHelper.GetDirfiles(dataDir)
    for index in range(0, len(listFiles)):
        fileName = listFiles[index]
        filePath = PathHelper.CombinePathpurely(dataDir, fileName)
        print(filePath)
        if os.path.isfile(filePath):
            pass
        else:
            print(filePath + "is a folder")
            #pro = Process(target=ExtractFolders,args=(filePath, listFolders,))
    return listFolders






if __name__ == "__main__":

    pathDir = r'\\192.168.30.89\share\第31次南极考察原始数据'
    #pathDir = r'C:\Users\chenlu\Desktop\tests\test0920\test1'
    pathDir = ReHelper.replacePath(pathDir)
    #listFolders = []
    #listFolders = ExtractFolders(pathDir,listFolders)
    listThreads = []
    parentProcessid = os.getpid()

    log = Logging.CreateLog()
    log.PrepareWrite('Parent process is %s' % parentProcessid)


    tarDir = r'C:\Users\chenlu\Desktop\word Version\words\south_31'
    tarDir = ReHelper.replacePath(tarDir)
    # list = threading.enumerate()
    # print('the number is %s' % (thCount))
    # test = os.getcwd()
    # test = os.path.dirname(tarDir)
    # test_Dir = os.path.abspath(test)
    #MergeFiles(pathDir,tarDir,['.docx','.doc'],0)
    #MergeFiles(pathDir, tarDir,'.docx',0)
    # os.listdir(pathDir)
    # print len(os.listdir(pathDir))
    try:
        Extractfiles(pathDir,tarDir,['.docx','.doc'],log,listThreads)
        log.PrepareWrite("-------the MainThread is already assign OK-------")
        for item in listThreads:
            log.PrepareWrite("%s must be OK" % (item.name))
            item.join()
        fileCount = len(GetDirfiles(tarDir))
        log.PrepareWrite("the count of folders is %s" % (fileCount))
        log.fileWrite()
        log.Close()
        # while True:
        #     log.PrepareWrite("STATUS CONFIRM")
        #     status = 0
        #     # for item in listThreads:
        #     #     print('threads: %s' % (item.name))
        #     print ('the thread count is %s' % (len(listThreads)))
        #
        #     for item in listThreads:
        #         item.join()
        #         if item.is_alive():
        #             print(item.name+" is alive")
        #             status = 1
        #             break
        #     if status == 0:
        #         log.PrepareWrite("all the folders has been searched")
        #         fileCount = len(GetDirfiles(tarDir))
        #         log.PrepareWrite("the count of folders is %s" % (fileCount))
        #         log.fileWrite()
        #         log.Close()
        #         break
        #     time.sleep(1)
    except Exception as err:
        print(err)
        fileCount = len(GetDirfiles(tarDir))
        log.PrepareWrite("the count of folders is %s" % (fileCount))
        log.fileWrite()
        log.Close()
    print ("OK")
