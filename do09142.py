import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
sys.path.append("D:/Applications/Python3/dataFileHelper")
from GeneralFunction import ReHelper,TableHelper,PathHelper,FileHelper,Logging,ListHelper
from dataFileHelper import WordHelper,ExcelHelper
import pandas as pd
import psycopg2
# filePath = r'C:\Users\chenlu\Desktop\word Version\test\south33_register1.xls'
# filePath = ReHelper.replacePath(filePath)
# listHead = ['uuid','pdfName','expName','wordName','DataName','projectName','projectperName','subjectName','subjectperName']
# df = pd.read_excel(filePath, names=listHead)
# for uuid in df.uuid:
#     x = df[df.uuid == uuid]['DataName']
#    # title = list(df[df.uuid == uuid]['title'])[0]
#     print (x)
#
# print("2")