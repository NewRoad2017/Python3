import sys
sys.path.append("D:/Applications/Python3/GeneralFunction")
sys.path.append("D:/Applications/Python3/dataFileHelper")
sys.path.append("D:/Applications/Python3/DataRescue")
from GeneralFunction import ReHelper,TableHelper,PathHelper,FileHelper,Logging,StringHelper
from dataFileHelper import WordHelper,ExcelHelper

class Template():
    def __init__(self):
        pass
    def getFromWord(self,dataPath):
        word = WordHelper.Word()
        word.fileRead(dataPath)
        if word.tableCount > 0:
            table = word.GetuniTable(0,0)
            listRows = table.listTableRows
            self.__title = listRows[0][1]
            self.__element = listRows[1][1]
            self.__instruid = listRows[2][1][3:]
            self.__instruName = listRows[2][3][3:]
            self.__keywords = StringHelper.Join(',',listRows[3][1],listRows[3][2],listRows[3][3],listRows[3][4],listRows[3][5],listRows[3][6])
            self.__longitude = listRows[4][5][3:]
            self.__latitude = listRows[4][1][3:]
            self.__highMax = listRows[5][1][3:]
            self.__highMin = listRows[5][5][3:]
            self.__datetimeStart = listRows[6][1][3:]
            self.__datetimeEnd = listRows[6][5][3:]
            self.__size = listRows[7][1][3:]
            self.__analyzeName = listRows[8][1][5:]
            self.__analyzeDate = listRows[9][1][6:]
            self.__metadataName = listRows[10][1][3:]
            self.__metadataTelephone = listRows[10][5][3:]
            self._get_metadataFax = listRows[11][1][3:]
            self.__metadataEmail = listRows[11][5][3:]
            self.__metadataAddr  = listRows[12][1][5:]
            self.__dataName = listRows[13][1][3:]
            self.__dataTelephone = listRows[13][5][3:]
            self.__dataFax = listRows[14][1][3:]
            self.__dataEmail = listRows[14][5][3:]
            self.__dataAddr = listRows[15][1][5:]
            self.__projName = listRows[17][1]
            self._get_projOfficer = listRows[17][8]
            self.__subprojName = listRows[16][1]
            self.__subprojOfficer = listRows[16][8]
            self.__remark = listRows[18][1]
            self.__signedBy = listRows[19][1][6:]
            (string, tupIndexs) = ReHelper.SearchPattern('日期', listRows[19][1])
            self.__signedDate = listRows[19][1][tupIndexs[1]+1:]
            self.dataType = 0


            # dataName = rowName[1]
            # listRecord = [filePath, filename, dataName]
            # listRecords.append(listRecord)

    def _get_title(self):
        return self.__title
    def _set_title(self,value):
        self.__title = value
    title = property(_get_title,_set_title)
    def _get_projName(self):
        return self.__projName
    def _set_projName(self,value):
        self.__projName = value
    projName = property(_get_projName,_set_projName)

    def _get_projOfficer(self):
        return self.__projOfficer
    def _set_projOfficer(self, value):
        self.__projOfficer = value
    projOfficer = property(_get_projOfficer, _set_projOfficer)

    def _get_subprojName(self):
        return self.__subprojName
    def _set_subprojName(self, value):
        self.__subprojName = value
    subprojName = property(_get_subprojName, _set_subprojName)

    def _get_subprojOfficer(self):
        return self.__subprojOfficer
    def _set_subprojOfficer(self, value):
        self.__subprojOfficer = value
    subprojOfficer = property(_get_subprojOfficer, _set_subprojOfficer)

    def _get_element(self):
        return self.__element
    def _set_element(self, value):
        self.__element = value
    element = property(_get_element, _set_element)

    def _get_instruid(self):
        return self.__instruid
    def _set_instruid(self, value):
        self.__instruid = value
    instruid = property(_get_instruid, _set_instruid)

    def _get_instruName(self):
        return self.__instruName
    def _set_instruName(self, value):
        self.__instruName = value
    instruName = property(_get_instruName, _set_instruName)

    def _get_keywords(self):
        return self.__keywords
    def _set_keywords(self, value):
        self.__keywords = value
    keywords = property(_get_keywords, _set_keywords)

    def _get_longitude(self):
        return self.__longitude

    def _set_longitude(self, value):
        self.__longitude = value

    longitude = property(_get_longitude, _set_longitude)

    def _get_latitude(self):
        return self.__latitude

    def _set_latitude(self, value):
        self.__latitude = value

    latitude = property(_get_latitude, _set_latitude)

    def _get_highMax(self):
        return self.__highMax

    def _set_highMax(self, value):
        self.__highMax = value

    highMax = property(_get_highMax, _set_highMax)

    def _get_highMin(self):
        return self.__highMin

    def _set_highMin(self, value):
        self.__highMin = value

    highMin = property(_get_highMin, _set_highMin)

    def _get_datetimeStart(self):
        return self.__datetimeStart

    def _set_datetimeStart(self, value):
        self.__datetimeStart = value

    datetimeStart = property(_get_datetimeStart, _set_datetimeStart)

    def _get_datetimeEnd(self):
        return self.__datetimeEnd

    def _set_datetimeEnd(self, value):
        self.__datetimeEnd = value

    datetimeEnd = property(_get_datetimeEnd, _set_datetimeEnd)

    def _get_size(self):
        return self.__size

    def _set_size(self, value):
        self.__asize = value

    size = property(_get_size, _set_size)

    def _get_analyzeName(self):
        return self.__analyzeName

    def _set_analyzeName(self, value):
        self.__analyzeName = value

    analyzeName = property(_get_analyzeName, _set_analyzeName)

    def _get_analyzeDate(self):
        return self.__analyzeDate

    def _set_analyzeDate(self, value):
        self.__analyzeDate = value

    analyzeDate = property(_get_analyzeDate, _set_analyzeDate)

    def _get_metadataName(self):
        return self.__metadataName

    def _set_metadataName(self, value):
        self.__metadataName = value

    metadataName = property(_get_metadataName, _set_metadataName)

    def _get_metadataTelephone(self):
        return self.__metadataTelephone

    def _set_metadataTelephone(self, value):
        self.__metadataTelephone = value

    metadataTelephone = property(_get_metadataTelephone, _set_metadataTelephone)

    def _get_metadataFax(self):
        return self.__metadataFax

    def _set_metadataFax(self, value):
        self.__metadataFax = value

    metadataFax = property(_get_metadataFax, _set_metadataFax)

    def _get_metadataEmail(self):
        return self.__metadataEmail

    def _set_metadataEmail(self, value):
        self.__metadataEmail = value

    metadataEmail = property(_get_metadataEmail, _set_metadataEmail)

    def _get_metadataAddr(self):
        return self.__metadataAddr

    def _set_metadataAddr(self, value):
        self.__metadataAddr = value

    metadataAddr = property(_get_metadataAddr, _set_metadataAddr)

    def _get_dataName(self):
        return self.__dataName

    def _set_dataName(self, value):
        self.__dataName = value

    dataName = property(_get_dataName, _set_dataName)

    def _get_dataTelephone(self):
        return self.__dataTelephone

    def _set_dataTelephone(self, value):
        self.__dataTelephone = value

    dataTelephone = property(_get_dataTelephone, _set_dataTelephone)

    def _get_dataFax(self):
        return self.__dataFax

    def _set_dataFax(self, value):
        self.__dataFax = value

    dataFax = property(_get_dataFax, _set_dataFax)

    def _get_dataEmail(self):
        return self.__dataEmail

    def _set_dataEmail(self, value):
        self.__dataEmail = value

    dataEmail = property(_get_dataEmail, _set_dataEmail)

    def _get_dataAddr(self):
        return self.__dataAddr

    def _set_dataAddr(self, value):
        self.__dataAddr = value

    dataAddr = property(_get_dataAddr, _set_dataAddr)

    def _get_remark(self):
        return self.__remark

    def _set_remark(self, value):
        self.__remark = value

    remark = property(_get_remark, _set_remark)
    def _get_signedBy(self):
        return self.__signedBy

    def _set_signedBy(self, value):
        self.__signedBy = value

    signedBy = property(_get_signedBy, _set_signedBy)

    def _get_signedDate(self):
        return self.__signedDate

    def _set_signedDate(self, value):
        self.__signedDate = value

    signedDate = property(_get_signedDate, _set_signedDate)

    def _get_coordinateDate(self):
        return self.__coordinateDate

    def _set_coordinateDate(self, value):
        self.__coordinateDate = value

    coordinateDate = property(_get_coordinateDate, _set_coordinateDate)

    def _get_dataType(self):
        return self.__dataType

    def _set_dataType(self, value):
        self.__dataType = value

    dataType = property(_get_dataType, _set_dataType)

if __name__ == '__main__':
    filePath = r'C:\Users\chenlu\Desktop\word Version\south_33_register\257.docx'
    filePath = ReHelper.replacePath(filePath)
    register = Template()
    register.getFromWord(filePath)
    pass


