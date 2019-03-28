import psycopg2

class dbconnection:
    def __init__(self,database = "systemmonitor",user = "systemmonitor",password = "Yargitay123",host = "10.6.212.61",port = "5432"):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def conn(self):
        baglanti = psycopg2.connect(database=self.database,user=self.user,password = self.password,host= self.host,port = self.port)
        return baglanti

    def __str__(self):
        return ("Baglanti OK")
