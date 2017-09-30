__author__ = "chenlu"
#the table should has the Head,the listRows
#the type of the datas in the table should be str
class Table:
    def __init__(self, dataName, dataTableRows, dataTableHead):
        self.name = dataName
        self.listTableRows = dataTableRows
        self.listTableHead = dataTableHead
        self.rowCount = len(self.listTableRows)
        self.colCount = len(self.listTableHead)
        if self.colCount > 0:
            self.__standarize()

    def __standarize(self):
        listRows = []
        for indexRow in range(0,self.rowCount):
            rowCur = self.listTableRows[indexRow]
            rowColCount = len(rowCur)
            listRowitems = []
            if rowColCount <self.colCount:
                for indexItem in range(0,rowColCount):
                    listRowitems.append(rowCur[indexItem])
                for indexItemEx in range(rowColCount,self.colCount):
                    listRowitems.append("")
            else:
                for indexItem in range(0, self.colCount):
                    listRowitems.append(rowCur[indexItem])
            listRows.append(listRowitems)
        self.listTableRows = listRows


    def GetlistCols(self):
        listCols = []
        for indexRow in range(0,self.rowCount):
            rowCur = self.listTableRows[indexRow]
            if indexRow == 0:
                for index in range(0,self.colCount):
                    listColparts = []
                    listColparts.append(rowCur[index])
                    listCols.append(listColparts)
            else:
                for index in range(0, self.colCount):
                    listCols[index].append(rowCur[index])
        self.listTableCols = listCols

    def GetuniCol(self,index):
        listColparts = []
        for indexRow in range(0,self.rowCount):
            rowCur = self.listTableRows[indexRow]
            listColparts.append(rowCur[index])
        return listColparts

    def GetsubTable(self, dataListColindexs):
        listRows = []
        for row in self.listTableRows:
            listRowitems = []
            for indexCol in dataListColindexs:
                item = row[indexCol]
                listRowitems.append(item)
            listRows.append(listRowitems)
        return "subTable", dataListColindexs, listRows







if __name__ == '__main__':
    listHead = list(range(1,5))
    listRows = [[m for m in 'ABCD'],[n for n in 'AB'],[s for s in 'A']]
    table = Table("test",listRows,listHead)
    table.GetlistCols()

    # listCols = table.listTableCols
    # listColCur = table.GetuniCol(2)
    # (subTablename,listHead,listRows) = table.GetsubTable([0,1])
    print(table)

    print (2)
