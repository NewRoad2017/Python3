import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
sys.path.append("D:/Applications/Python3/dataFileHelper")
sys.path.append("D:/Applications/Python3/DataRescue")
from GeneralFunction import ReHelper,TableHelper,PathHelper,FileHelper,Logging
from dataFileHelper import WordHelper,ExcelHelper
from DataRescue import DataSamRegister
#get the word and the dataName
def getRecord(dataPath,dataName,dataList):
    word = WordHelper.Word()
    word.fileRead(dataPath)
    if word.tableCount > 0:
        table = word.GetuniTable(0)
        listRows = table.listTableRows
        title = listRows[0][1]
        listRecord = [dataPath, dataName, title]
        dataList.append(listRecord)
        return True
    else:
        return False

if __name__ == '__main__':
    # create log
    logDir = r'C:\Users\chenlu\Desktop\logs'
    log = Logging.Logging.CreateLog(logDir)

    # create every model
    fileDir = r"C:\Users\chenlu\Desktop\word Version\test\south_33_register"
    fileDir = ReHelper.replacePath(fileDir)
    listFiles = FileHelper.GetDirfiles(fileDir)
    listRecords = []
    for filename in listFiles:
        print(filename)
        filePath = PathHelper.CombinePathpurely(fileDir, filename)
        log.PrepareWrite(filePath)
        status = getRecord(filePath,filename,listRecords)
        if status == False:
            tarfilePath = r"C:\Users\chenlu\Desktop\word Version\south_33_noOpen"
            tarfilePath = ReHelper.replacePath(tarfilePath)
            FileHelper.MoveFile(filePath, tarfilePath)
    table = TableHelper.Table("onlyname", list(range(3)), listRecords)
    filePathExcel = r'C:\Users\chenlu\Desktop\tests\intergration.xls'
    filePathExcel = ReHelper.replacePath(filePathExcel)
    excelWrite = ExcelHelper.ExcelWrite(filePathExcel, [table])

    print("OK")