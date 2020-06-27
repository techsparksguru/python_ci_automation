import sqlite3
from sqlite3 import Error


class DBHelper:
    
    def __init__(self, filedb='db/pythonsqlite3.db'):
        self.filedb=filedb

    def __connect__(self):
        try:
            self.con = sqlite3.connect(self.filedb)
            self.cur = self.con.cursor()
        except Error as e:  
            print(e)

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.con.commit()
        self.__disconnect__()

    def manipulate(self, sql, task):
        self.__connect__()
        self.cur.execute(sql, task)
        self.con.commit()
        self.__disconnect__()
        return self.cur.lastrowid

