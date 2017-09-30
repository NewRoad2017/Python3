import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
sys.path.append("D:/Applications/Python3/dataFileHelper")
from GeneralFunction import ReHelper,TableHelper,PathHelper,FileHelper,Logging,ListHelper
from dataFileHelper import WordHelper,ExcelHelper
#create log
logPath = r'C:\Users\chenlu\Desktop\logs'
logPath = ReHelper.replacePath(logPath)
log = Logging.Logging(logPath)

filePath = r'C:\Users\chenlu\Desktop\word Version\south_33last.xlsx'
filePath = ReHelper.replacePath(filePath)
excel = ExcelHelper.ExcelRead(filePath)
listpdfMatch1 = excel.GetListFromCol(0,3)
listpdfLast = ListHelper.CleantheNull(listpdfMatch1)
ListHelper.Sort(listpdfLast)
log.PrepareWrite("the match count is " + str(len(listpdfLast)))
for item in listpdfLast:
    log.PrepareWrite(item)

log.PrepareWrite("----------")

#read the origin
filePath = r'C:\Users\chenlu\Desktop\word Version\test\intergration.xls'
filePath = ReHelper.replacePath(filePath)
excel = ExcelHelper.ExcelRead(filePath)
listWords1 = excel.GetListFromCol(0,1)
listWord2 = ListHelper.CleantheNull(listWords1)
ListHelper.Sort(listWord2)
log.PrepareWrite("the word count is " + str(len(listWord2)))
for item in listWord2:
    log.PrepareWrite(item)
#compare shoould optimize
log.PrepareWrite("-----------")


count = 0
for item in listWord2:
    status = 0
    for itemM in listpdfLast:
        if item == itemM:
            status = 1
            break
    if status == 0:
        log.PrepareWrite(item)
        count = count+1
log.PrepareWrite(str(count))




log.Close()
print ("OK")