##
#this py is a functin program,
import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
sys.path.append("D:/Applications/Python3/dataFileHelper")
sys.path.append("D:/Applications/Python3/Data")
from GeneralFunction import ReHelper,TableHelper,PathHelper,FileHelper,Logging,ListHelper
from dataFileHelper import WordHelper,ExcelHelper
from Data import PostgresqlHelper
import pandas as pd

#create log
logPath = r'C:\Users\chenlu\Desktop\logs'
logPath = ReHelper.replacePath(logPath)
log = Logging.Logging(logPath)

#get the uuid from the databas
postgresql = PostgresqlHelper.Postgresql()
log.PrepareWrite("postgresql is OK")
strSQL= 'select id from exp_system.exp_dataregistertemplog'
log.PrepareWrite("postgresql:Query", strSQL)
listRows = postgresql.Query(strSQL)
postgresql.Commit()
log.PrepareWrite("The result is:")
listUUIDs=[]
for id in listRows:
    listUUIDs.append(str(id[0]))
    log.PrepareWrite(str(id[0]))


#get the table from the excel
filePath = r'C:\Users\chenlu\Desktop\word Version\test\south33_register1.xls'
filePath = ReHelper.replacePath(filePath)
log.PrepareWrite("Read the excel:", filePath)
listHead = ['uuid','pdfName','expName','wordName','title','projName','projOfficer','subprojName','subprojOfficer']
df = pd.read_excel(filePath, names=listHead)
for uuid in df.uuid:
    print (uuid)
    log.PrepareWrite("uuid:", str(uuid))
    title = str(list(df[df.uuid == uuid]['title'])[0])# This word is hard to understand
    projName = str(list(df[df.uuid == uuid]['projName'])[0])
    projOfficer = str(list(df[df.uuid == uuid]['projOfficer'])[0])
    subprojName = str(list(df[df.uuid == uuid]['subprojName'])[0])
    subprojOfficer = str(list(df[df.uuid == uuid]['subprojOfficer'])[0])
    log.PrepareWrite("info:", title, projName, projOfficer, subprojName, subprojOfficer)
    strSQL = "update exp_system.temp_sampledata set state='已保存',userid = 'NewRoad2017' where id='%s';" % (uuid)
    log.PrepareWrite("postgresql:Update", strSQL)
    postgresql.Update(strSQL)
    log.PrepareWrite("postgresql:Update OK")
    if uuid in listUUIDs:
        log.PrepareWrite(str(uuid), "is in the dataBase")
        strSQL = """update exp_system.exp_dataregistertemplog set title='%s',"projName" = '%s',"projOfficer" = '%s',"subprojName" = '%s',"subprojOfficer" = '%s' where id='%s';""" % (title,projName,projOfficer,subprojName,subprojOfficer,uuid)
        log.PrepareWrite("postgresql:Update", strSQL)
        postgresql.Update(strSQL)
        log.PrepareWrite("postgresql:Update OK")
    else:
        log.PrepareWrite(str(uuid), "is not in the dataBase")
        strSQL = """insert into exp_system.exp_dataregistertemplog(id,title,"projName","projOfficer","subprojName","subprojOfficer") values('%s','%s','%s','%s','%s','%s');""" % (uuid, title, projName, projOfficer, subprojName, subprojOfficer)
        log.PrepareWrite("postgresql:Insert", strSQL)
        postgresql.Insert(strSQL)
        log.PrepareWrite("postgresql:Insert OK")
postgresql.Close()
log.Close()
print (2)