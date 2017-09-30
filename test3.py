import psycopg2

__database = "mydb"
__user = "" # write yourself
__password = "" # write yourself
__host = "127.0.0.1"
__port = "5432"
if __name__ == '__main__':
    conn = psycopg2.connect(database=__database, user=__user, password=__password,
                                 host=__host, port=__port)
    cur = conn.cursor()
    print(2)