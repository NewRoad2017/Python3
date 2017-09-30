import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
sys.path.append("D:/Applications/Python3/dataFileHelper")
from GeneralFunction import ReHelper,TableHelper,PathHelper,FileHelper,Logging
from dataFileHelper import WordHelper
def JudgesoMove(dataJudge,dataOriPath,dataListType,datalistTarDirs):
    for index in range(0, len(dataListType)):
        result = ReHelper.SearchPattern(dataListType[index], dataJudge)
        if result:
            tarDir = datalistTarDirs[index]
            tarPath = PathHelper.CombinePathpurely(tarDir, filename)
            log.PrepareWrite("Move to" + tarDir)
            FileHelper.MoveFile(dataOriPath, tarPath)
            break
#create log
logPath = r'C:\Users\chenlu\Desktop\logs'
logPath = ReHelper.replacePath(logPath)
log = Logging.Logging(logPath)

#create every model
listType = ['注册表','提交表']
fileDir = r"C:\Users\chenlu\Desktop\word Version\test\south_33_1"
fileDir = ReHelper.replacePath(fileDir)
listFiles = FileHelper.GetDirfiles(fileDir)
listTarDirs = [ReHelper.replacePath(r'C:\Users\chenlu\Desktop\word Version\test\south_33_register'),ReHelper.replacePath(r'C:\Users\chenlu\Desktop\word Version\test\south_33_submit')]

for filename in listFiles:
    print (filename)
    filePath = PathHelper.CombinePathpurely(fileDir,filename)
    log.PrepareWrite(filePath)
    word = WordHelper.WordRead(filePath)
    # wether it is a submit or a register
    paraCount = word.paragraphCount
    if paraCount == 0:
        pass
    elif paraCount == 1:
        title = word.listParagraphs[0].text
        JudgesoMove(title,filePath,listType,listTarDirs)
    else:
        for i in [0,1]:
            title = word.listParagraphs[i].text
            JudgesoMove(title, filePath, listType, listTarDirs)

log.Close()
print(2)
