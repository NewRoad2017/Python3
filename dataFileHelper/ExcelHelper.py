__author__ = "chenlu"

import xlwt
import xlrd
import csv
import os
from xlutils.copy import copy
import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
from GeneralFunction import ReHelper,TableHelper



class Excel:
    def _get_filePath(self):
        return self.__filePath
    def _set_filePath(self,value):
        self.__filePath = value
    filePath = property(_get_filePath,_set_filePath)

    def _get_listTable(self):
        return self.__listTable
    def _set_listTable(self,value):
        self.__listTable = value
    listTable = property(_get_listTable,_set_listTable)

    def __init__(self):
        self.workbook = None
        self.sheets = []
        self.listTables = []

    def fileRead(self):
        try:
            self.workbook = xlrd.open_workbook(self.__filePath)
            self.sheets = self.workbook.sheets()
        except Exception as e:
            print(str(e))
            sys.exit()
    def fileWrite(self,dataListTables = None):
        if dataListTables is not None:
            self.listTables = dataListTables


    def GetuniTable(self, index, dataHasHead):
        sheetCur = self.sheets[index]
        name = sheetCur.name
        rowcount = sheetCur.nrows
        colcount = sheetCur.ncols
        listHeadparts = []
        listRows = []
        if dataHasHead == 1:
            for row in range(0, rowcount):
                if row == 0:
                    for col in range(0, colcount):
                        value = sheetCur.cell(row, col).value
                        listHeadparts.append(value)
                else:
                    listRowParts = []
                    for col in range(0, colcount):
                        value = sheetCur.cell(row, col).value
                        listRowParts.append(value)
                    listRows.append(listRowParts)
            table = TableHelper.Table(name, listRows, dataHasHead, listHeadparts)
        else:
            for row in range(0, rowcount):
                listRowParts = []
                for col in range(0, colcount):
                    value = sheetCur.cell(row, col).value
                    listRowParts.append(value)
                listRows.append(listRowParts)
            table = TableHelper.Table(name, listRows, dataHasHead, listHeadparts)
        return table

    def __setExcel(self):
        try:
            self.workbook = xlwt.Workbook()
            for table in self.listTables:
                sheet = self.workbook.add_sheet(table.name)
                rowCount = table.rowCount
                colCount = table.colCount
                if table.listTableHead is not []:
                    for index in range(0, colCount):
                        sheet.write(0, index, table.listTableHeadparts[index])
                    for row in range(0, rowCount):
                        for col in range(0, colCount):
                            sheet.write(row + 1, col, table.listTableRows[row][col])
                else:
                    for row in range(0, rowCount):
                        for col in range(0, colCount):
                            sheet.write(row, col, table.listTableRows[row][col])
                self.sheets.append(sheet)
            self.workbook.save(self.filePath)
        except Exception as e:
            print(self.__setExcel.__name__)
            print(str(e))
            sys.exit()


class ExcelRead(Excel):
    def __init__(self, dataPath):
        Excel.__init__(self, dataPath)
        self.__getExcel()

    def __getExcel(self):
        try:
            self.workbook = xlrd.open_workbook(self.filePath)
            self.sheets = self.workbook.sheets()
            #self.listTables = []
        except Exception as e:
            print(str(e))
            sys.exit()



    def GetuniTable(self,index,dataHasHead):
        sheetCur = self.sheets[index]
        name = sheetCur.name
        rowcount = sheetCur.nrows
        colcount = sheetCur.ncols
        listHeadparts = []
        listRows = []
        if dataHasHead == 1:
            for row in range(0, rowcount):
                    if row == 0:
                        for col in range(0, colcount):
                            value = sheetCur.cell(row, col).value
                            listHeadparts.append(value)
                    else:
                        listRowParts = []
                        for col in range(0, colcount):
                            value = sheetCur.cell(row, col).value
                            listRowParts.append(value)
                        listRows.append(listRowParts)
            table = TableHelper.Table(name, listRows,dataHasHead,listHeadparts)
        else:
            for row in range(0, rowcount):
                listRowParts = []
                for col in range(0, colcount):
                    value = sheetCur.cell(row, col).value
                    listRowParts.append(value)
                listRows.append(listRowParts)
            table = TableHelper.Table(name, listRows,dataHasHead,listHeadparts)
        return table





    # def excel2Table(self):
    #     for sheet in self.sheets:
    #         name = sheet.name
    #         rowcount = sheet.nrows
    #         colcount = sheet.ncols
    #         listHeadparts = []
    #         listRows = []
    #         for row in range(0, rowcount):
    #             if row == 0:
    #                 for col in range(0, colcount):
    #                     value = sheet.cell(row, col).value
    #                     listHeadparts.append(value)
    #             else:
    #                 listRowParts = []
    #                 for col in range(0, colcount):
    #                     value = sheet.cell(row, col).value
    #                     listRowParts.append(value)
    #                 listRows.append(listRowParts)
    #         table = TableHelper.Table(name, listHeadparts, listRows)
    #         self.listTables.append(table)
    #
    # def GetListFromCol(self,dataTableIndex,index):
    #     table = self.listTables[dataTableIndex]
    #     table.GetlistCols()
    #     list = table.listCols[index]
    #     return list



class ExcelWrite(Excel):
    def __init__(self, dataPath, dataListTables):
        Excel.__init__(self,dataPath)
        self.listTables = dataListTables
        self.__setExcel()

    def __setExcel(self):
        try:
            self.workbook = xlwt.Workbook()
            for table in self.listTables:
                sheet = self.workbook.add_sheet(table.name)
                rowCount = table.rowCount
                colCount = table.colCount
                if table.hasHead == 1:
                    for index in range(0, colCount):
                        sheet.write(0, index, table.listTableHeadparts[index])
                    for row in range(0, rowCount):
                        for col in range(0, colCount):
                            sheet.write(row+1, col, table.listTableRows[row][col])
                else:
                    for row in range(0, rowCount):
                        for col in range(0, colCount):
                            sheet.write(row, col, table.listTableRows[row][col])
                self.sheets.append(sheet)
            self.workbook.save(self.filePath)
        except Exception as e:
            print (self.__setExcel.__name__)
            print (str(e))
            sys.exit()




# class Excelappend(Excel):
#     def __init__(self,dataFilepath,sheetid):
#         Excel(dataFilepath)
#
#     def __appendExcel(self):
#         try:
#             self.workbook = copy(xlrd.open_workbook(self.filePath))
#             self.sheets = self.workbook.sheets()
#             self.listinfos = []
#         except Exception as e:
#             print str(e)
#             sys.exit()

if __name__ == '__main__':

    # filePath = r'C:\Users\chenlu\Desktop\word Version\south_33last.xlsx'
    # filePath = ReHelper.replacePath(filePath)
    # excel = ExcelRead(filePath)
    # table = excel.GetuniTable(0,0)


    filePath = r'C:\Users\chenlu\Desktop\word Version\test\test.xls'
    filePath = ReHelper.replacePath(filePath)
    tableTest = TableHelper.Table("test",[['SS','DD','XX']],0,['H1','H2','H3'])
    excel = ExcelWrite(filePath,[tableTest])




