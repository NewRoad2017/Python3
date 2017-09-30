import time
import sys
sys.path.append('D:/Applications/Python3/GeneralFunction')
from GeneralFunction import PathHelper,ReHelper
sys.path.append('D:/Applications/Python3/dataFileHelper')
from dataFileHelper import TXT

class Logging(object):
    def __init__(self,dataDir):
        strTime = time.strftime('%Y%m%d_%H_%M_%S',time.localtime(time.time()))
        self.filePath = PathHelper.CombinePathpurely(dataDir,'logging'+strTime+'.txt')
        self.txtFile = TXT()

    def PrepareWrite(self, *args):
        for arg in args:
            self.txtFile.Append2List(arg)
            print(arg)

    def fileWrite(self):
        self.txtFile.fileWrite( self.filePath )

    def Close(self):
        self.txtFile.Close()

    @classmethod
    def CreateLog(cls,dataDir = r'C:\Users\chenlu\Desktop\logs'):
        dataDir = ReHelper.replacePath(dataDir)
        log = Logging(dataDir)
        return log


if __name__ == '__main__':
    log = Logging.CreateLog()
    log.PrepareWrite("Hello Road~")
    log.PrepareWrite("hh~")
    log.PrepareWrite("Hello Road~")
    log.PrepareWrite("hh~")
    log.fileWrite()
    log.Close()
    print (2)