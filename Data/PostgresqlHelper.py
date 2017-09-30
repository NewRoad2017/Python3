__author__ = "chenlu"
__author_email = "385134634@qq.com"
import sys
sys.path.append('D:/Applications/Python3/dataFileHelper')
sys.path.append('D:/Applications/Python3/GeneralFunction')
import  psycopg2
__all__ = ['Postgresql']
class Postgresql:
    # __database="chinare"
    # __user="v2"
    # __password="Pric@chinare_v2"
    # __host="192.168.10.99"
    # __port="5432"
    __database="mydb"
    __user="chenlu"
    __password="BRANDY"
    __host="127.0.0.1"
    __port="5432"
    def __init__(self):
        self.conn = psycopg2.connect(database=Postgresql.__database, user=Postgresql.__user, password=Postgresql.__password, host=Postgresql.__host, port=Postgresql.__port)
        self.cur = self.conn.cursor()

    def SetSQL(self,dataTable,*args,dataSQL = None,**kwargs):
        strSQL = ""
        if dataSQL != None:
            strSQL = dataSQL
        else:
            strSQL = "select "
            strWhere = "where "
            for index, item in enumerate(args):
                strSQL = strSQL + item
                if index != len(args) - 1:
                    strSQL = strSQL + ","
                else:
                    strSQL = strSQL + " "
            strSQL = strSQL + "from %s " % dataTable
            for index, item in enumerate(kwargs.items()):
                key = item[0]
                value = item[1]
                if isinstance(value, str):
                    strWhere = strWhere + "%s like '%s' " % (key, value)
                else:
                    strWhere = strWhere + "%s = %s " % (key, value)
                if index == len(kwargs) - 1:
                    strWhere = strWhere + " and "
        return strSQL

    def RevisestrSQL(self,dataSQL):
        pass


    def Query(self,dataSQL):
        self.cur.execute(dataSQL)
        listRows = self.cur.fetchall()
        return listRows

    def Insert(self,dataSQL):
        self.cur.execute(dataSQL)
        self.Commit()
        # dict1 = dict(dataDict)
        # strSQLPart1 = "insert into %s ( " % dataTable
        # strSQLPart2 = "values ( "
        # for k,v in dict1.items():
        #     strSQLPart1 = strSQLPart1 + '%s,' % k
        #     strSQLPart2 = strSQLPart2 + ''



    def Update(self, dataSQL):
        self.cur.execute(dataSQL)
        self.Commit()



    def GetTableFields(self,dataTable):
        str = "SELECT col_description(a.attrelid,a.attnum) as comment,format_type(a.atttypid,a.atttypmod) as type,a.attname as name, a.attnotnull as notnull  FROM pg_class as c,pg_attribute as a where c.relname = '% s' and a.attrelid = c.oid and a.attnum>0" % dataTable
        self.cur.execute(str)
        listRows = self.cur.fetchall()
        self.conn.commit()
        return listRows

    def GetoneList(self,dataSQL,index):
        listRecords = self.Query(dataSQL)
        list = []
        for record in listRecords:
            list.append(record[index])
        return list

    def GetoneDict(self,dataFieldKey,dataFieldValue,dataTable):
        sqlstr = "select %s, %s from %s" % (dataFieldKey,dataFieldValue,dataTable)
        listResult = self.Query(sqlstr)
        dictResult = dict(listResult)
        return dictResult



    def Commit(self):
        self.conn.commit()

    def Close(self):
        self.conn.close()


xx = 2
if __name__ == '__main__':
    postgresql = Postgresql()
    # result = postgresql.GetTableFields('exp_dataregistertemplog')
    # print (__author__)

    #result = postgresql.GetList("exp_system.exp_dataregistertemplog")
    print(2)
