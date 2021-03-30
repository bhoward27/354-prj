import mysql.connector
from pathlib import Path
from os import chdir

class Executor:
    def __init__(self):
        self.db = self.connectToDatabase()
        self.cursor = self.db.cursor()
        self.__setValidTableNames()

    def __del__(self):
        self.cursor.close()
        self.db.disconnect()
    
    @staticmethod
    def connectToDatabase():
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Fattest5!",
            database = "test_project",
        )
    
    def __setValidTableNames(self):
        self.validTableNames = []
        self.cursor.execute("SHOW TABLES;")
        results = self.cursor.fetchall()
        for result in results:
            self.validTableNames.append(result[0].lower())

    def insert(self, tableName, values):
        if not self.isValidTableName(tableName):
            print("ValueError: tableName '" + tableName + "' is invalid.")
            raise ValueError
        
        if not (isinstance(values, tuple) or isinstance(values, list)):
            print("TypeError: values must be a tuple, list of tuples, or tuple of tuples.")
            raise TypeError

        if self.hasTuple(values):
            for record in values:
                self.__insert(tableName, record)
            self.db.commit()
        else:
            self.__insert(tableName, values)
            self.db.commit()

    def __insert(self, tableName, record):
        if not isinstance(record, tuple) or self.hasTuple(record):
            print("TypeError: record = ", record, ", but needs to be a flat tuple.", sep = "")
            raise TypeError

        sql = "INSERT INTO " + tableName + " VALUES ("
        numColumns = len(record)
        for i in range(1, numColumns + 1):
            sql += "%s, "
        sql = sql[: len(sql) - 2] + ");"
        self.cursor.execute(sql, record)

    @staticmethod
    def hasTuple(x):
        return any(isinstance(i, tuple) for i in x)

    def isValidTableName(self, tableName):
        return tableName.lower() in self.validTableNames