import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
from GeneralFunction import ReHelper

class TXT:
    __status = 0
    def __init__(self):
        self.__listRows = []
        self.__listRowsNR = []

    def Close(self):
        self.file.close()

    def Append2List(self,dataRow):
        self.__listRows.append(dataRow)
        self.__listRowsNR.append(dataRow + '\n')

    def fileRead(self,dataPath):
        TXT.__status = 1
        self.filePath = dataPath
        self.file = open(self.filePath, 'r', encoding='utf-8')
        self.__listRowsNR = self.file.readlines()
        for row in self.__listRowsNR:
            row = ReHelper.subString(row,'\n','')
            self._append2List(row)

    def fileWrite(self,dataPath):
        TXT.__status = -1
        self.filePath = dataPath
        self.file = open(self.filePath, 'w', encoding='utf-8')
        for strRow in self.__listRowsNR:
            self.file.write(strRow)

    # def WriteRow(self,dataRowStr):
    #     if TXT.__status == -1:
    #         self._append2List(dataRowStr)
    #         self.file.write(dataRowStr+'\n')
    #
    # def __WriteLines(self, dataPath):
    #     for strRow in self.__listRowsNR:
    #         self.file.write(strRow)
#property
    def _set_listRows(self,value):
        self.__listRows = value
        for item in value:
            str = item + '\n'
            self.__listRowsNR.append(str)
    def _get_listRows(self):
        return self.__listRows
    listRows = property(_get_listRows,_set_listRows)

    def test(data):
        listRows = []
        str = 'def _get_%s(self):' % (data)
        listRows.append(str)
        str = '   return self.__%s' % (data)
        listRows.append(str)
        str = 'def _set_%s(self, value):' % (data)
        listRows.append(str)
        str = '   self.__%s = value' % (data)
        listRows.append(str)
        str = '%s = property(_get_%s, _set_%s)' % (data,data,data)
        listRows.append(str)
        return listRows



# class txtRead(TXT):
#     def __init__(self,dataPath):
#         TXT.__init__(self,dataPath)
#         self.fileRead = open(self.filePath,'r',encoding='utf-8')
#     def ReadLines(self):
#         self.listRows = self.fileRead.readlines()
#     def Read(self):
#         strContent = self.fileRead.read()
#         self.listRows = strContent.split('\n')
#     def Close(self):
#         self.fileRead.close()
#
# class txtWrite(TXT):
#     def __init__(self,dataPath):
#         TXT.__init__(self,dataPath)
#         self.fileWriteLines = open(self.filePath,'w',encoding='utf-8')
#     def Write(self,dataString):
#         self.fileWriteLines.write(dataString)
#     def Close(self):
#         self.fileWriteLines.close()


if __name__ == '__main__':
    txt = TXT()
    filePath = ReHelper.replacePath(r"C:\Users\chenlu\Desktop\tests\test0919\test.txt")
    txt.Append2List('Hello Road!~')
    txt.fileWrite(filePath)
    txt.Close()



    # txt = TXT()
    # txt.fileRead(r'C:\Users\chenlu\Desktop\logs\logging20170919_15_23_32.txt')
    # mode = txt.file
    # list = []
    # listFields = ['longitude','latitude','highMax','highMin','datetimeStart','datetimeEnd','analyzeName','analyzeDate','metadataName','metadataTelephone','metadataFax','metadataEmail','metadataAddr','dataName','dataTelephone','dataFax','dataEmail','dataAddr','signedBy','signedDate','coordinateDate','dataType']
    # for item in listFields:
    #     listRows = test(item)
    #     for row in listRows:
    #         list.append(row)
    #
    # filePath = r'C:\Users\chenlu\Desktop\tests\test1.txt'
    # filePath = ReHelper.replacePath(filePath)
    # txt = TXT()
    # txt.listRows = list
    # txt.fileWriteLines(filePath)
    # txt.fileWriteLines(filePath)
    # txt.Close()

    # data = txtread.fileRead.read()

    print ("2")


