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
        print("Valid table names: ", self.validTableNames)

    def insert(self, tableName, values):
        if not self.isValidTableName(tableName):
            print("ValueError: tableName '" + tableName + "' is invalid.")
            raise ValueError
        
        if (isinstance(values, tuple) or isinstance(values, list)) \
            and any(isinstance(x, tuple) for x in values):
            for record in values:
                self.__insert(tableName, record)
            self.db.commit()
        elif isinstance(values, tuple):
            self.__insert(tableName, values)
            self.db.commit()
        else:
            print("TypeError: values must be a tuple, list of tuples, or tuple of tuples.")
            raise TypeError

    def __insert(self, tableName, record):
        sql = "INSERT INTO " + tableName + " VALUES ("
        numColumns = len(record)
        for i in range(1, numColumns + 1):
            sql += "%s, "
        sql = sql[: len(sql) - 2] + ");"
        self.cursor.execute(sql, record)

    def isValidTableName(self, tableName):
        return tableName.lower() in self.validTableNames