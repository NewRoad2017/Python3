import sys
sys.path.append('D:/Applications/Python3/Data')
from Data import PostgresqlHelper
class PostgresqlRegister:
    def __init__(self):
        self.postgresql = PostgresqlHelper.Postgresql()