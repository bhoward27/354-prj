import mysql.connector
from pathlib import Path
from os import chdir

class Executor:
    def __init__(self):
        self.db = connectToDatabase()
        self.cursor = self.db.cursor()
        __setValidTableNames()

    def __del__(self):
        print("Running Cursor.__del__()...")
        self.cursor.close()
        self.db.disconnect()
    
    @staticmethod
    def connectToDatabase():
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Fattest5!",
            # database = "test_project",
        )
    
    def __setValidTableNames(self):
        self.validTableNames = []
        db.execute("SHOW TABLES;")
        results = db.fetchall()
        for result in results:
            self.validTableNames.append(result)
        print("Valid table names: ", self.validTableNames)

    def insert(self, tableName, values):
        if not isValidTableName(tableName):
            raise ValueError
        
    def isValidTableName(self, tableName):
        return tableName.lower() in self.validTableNames
