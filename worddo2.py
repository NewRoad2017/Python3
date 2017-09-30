import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
sys.path.append("D:/Applications/Python3/dataFileHelper")
from GeneralFunction import ReHelper,TableHelper,FileHelper,PathHelper,Logging
from dataFileHelper import WordHelper,ExcelHelper

#create log
logPath = r'C:\Users\chenlu\Desktop\logs'
logPath = ReHelper.replacePath(logPath)
log = Logging.Logging(logPath)
# 2. the first clear,put the big file out
fileDir = r'C:\Users\chenlu\Desktop\word Version\test\south_33_1'
fileDir = ReHelper.replacePath(fileDir)
tarFileDir = r'C:\Users\chenlu\Desktop\word Version\test\south_33_2'
tarFileDir = ReHelper.replacePath(tarFileDir)

listFiles = FileHelper.GetDirfiles(fileDir)
for filename in listFiles:
    filePath = PathHelper.CombinePathpurely(fileDir,filename)
    log.PrepareWrite(filePath)
    if PathHelper.GetFileSize(filePath) < 5 or PathHelper.GetFileSize(filePath)> 50:
        if PathHelper.GetFileSize(filePath) < 5:
            log.PrepareWrite('this file is too small')
        else:
            log.PrepareWrite('this file is too big')
        tarPath = PathHelper.CombinePathpurely(tarFileDir,filename)
        log.PrepareWrite('move to' + tarPath)
        FileHelper.MoveFile(filePath,tarPath)
log.Close()
print (2)