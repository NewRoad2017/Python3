import os
import sys
sys.path.append('D:/Applications/Python3/GeneralFunction')
from GeneralFunction import *
from shutil import copy
import threading
import time,random
import shutil
def extractExpTeamRegisters(dataDir,dataTarDir,dataDict):
    for dirName,tarName in dataDict.items():
        dirPath = PathHelper.CombinePathpurely(dataDir,dirName)
        tarPath = PathHelper.CombinePathpurely(dataTarDir,tarName)
        if os.path.exists(tarPath):
            shutil.rmtree(tarPath)
        FileHelper.MakeDir(tarPath)
        FileHelper.Extractfiles1(dirPath, tarPath, log, ['.docx', '.doc', ], [10, 100])




if __name__ == '__main__':
    timeB = time.clock()
    dict1 = {'第22次南极考察原始资料': 'south_22', '第24次南极考察原始资料': 'south_24', '第26次南极考察原始资料': 'south_26', '第27次南极考察原始资料': 'south_27',
     '第15次南极考察原始数据': 'south_15', '第21次南极考察原始数据': 'south_21', '第23次南极考察原始数据': 'south_23', '第26次南极考察原始数据': 'south_26',
     '第27次南极考察原始数据': 'south_27'}
    log = Logging.CreateLog()
    extractExpTeamRegisters(r'\\192.168.30.89\share',r'C:\Users\chenlu\Desktop\word Version\words',dict1)
    # fileDir = r'\\192.168.30.89\share\第25次南极考察原始数据'
    # fileDir = ReHelper.replacePath(fileDir)
    # fileTarDir = r'C:\Users\chenlu\Desktop\word Version\words\south_25_2'
    # fileTarDir = ReHelper.replacePath(fileTarDir)
    # # for a,b,c in os.walk(fileDir):
    # #     print (c)
    # FileHelper.Extractfiles1(fileDir,fileTarDir,log,['.docx','.doc',],[10,100])
    timeE = time.clock()
    log.PrepareWrite(str(timeE - timeB))
    log.fileWrite()
    log.Close()

