import sys
sys.path.append('D:/Applications/Python3/Data')
from Data import PostgersqlRegister,PostgresqlHelper
class DataAccess:
    dataBase = "Postgresql"
    @classmethod
    def CreateRegister(cls):
        result = PostgersqlRegister.PostgresqlRegister()
        str = cls.dataBase + "Register"
        exec("return new " + str)

