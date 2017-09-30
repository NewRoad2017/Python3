import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
sys.path.append("D:/Applications/Python3/dataFileHelper")
from GeneralFunction import ReHelper,TableHelper,PathHelper,FileHelper,Logging,ListHelper
from dataFileHelper import WordHelper,ExcelHelper
#create log
logPath = r'C:\Users\chenlu\Desktop\logs'
logPath = ReHelper.replacePath(logPath)
log = Logging.Logging(logPath)

#1.get the table :uuid,pdfName,wordName,DataName,projectName,projectperName,subjectName,subjectperName
#fileDir = 'C:\Users\chenlu\Desktop\word Version\test\south_33_register'
filePath = r'C:\Users\chenlu\Desktop\word Version\south_33last.xlsx'
filePath = ReHelper.replacePath(filePath)
excel = ExcelHelper.ExcelRead(filePath)
tableExcel = excel.GetuniTable(0,0)

listPdfUUIDs = tableExcel.GetuniCol(0)
listWordMnames = tableExcel.GetuniCol(3)
(listWordMnamesNonull,dictIndex) = ListHelper.CleantheNull(listWordMnames)

#from word
fileDir = r"C:\Users\chenlu\Desktop\word Version\test\south_33_register"
fileDir = ReHelper.replacePath(fileDir)
for index in range(0,len(listWordMnames)):
    item = listWordMnames[index]
    log.PrepareWrite("uuid: " + listPdfUUIDs[index])
    dataSamName = ""
    subjectName = ""
    subjectPerName = ""
    projectName = ""
    projectPerName = ""
    if item != "":
        print (item)
        log.PrepareWrite("MatchWord: " + item)
        path = PathHelper.CombinePathpurely(fileDir,item)
        word = WordHelper.WordRead(path)
        table = word.GetuniTable(0,0)
        dataSamName = table.listTableRows[0][1]
        subjectName = table.listTableRows[16][1]
        subjectPerName = table.listTableRows[16][8]
        projectName = table.listTableRows[17][1]
        projectPerName = table.listTableRows[17][8]
        log.PrepareWrite(dataSamName, subjectName, subjectPerName, projectName, projectPerName)
    ListHelper.ListAppend(tableExcel.listTableRows[index],subjectName,subjectPerName,projectName,projectPerName)#has the name

#toexcel
excelFilepath = r'C:\Users\chenlu\Desktop\word Version\test\inter.xls'
excelFilepath = ReHelper.replacePath(excelFilepath)
listHead = ['uuid','pdfName','expName','wordName','DataName','projectName','projectperName','subjectName','subjectperName']
table = TableHelper.Table("south_33",tableExcel.listTableRows,1,listHead)
excel = ExcelHelper.ExcelWrite(excelFilepath,[table])
log.Close()
print(2)