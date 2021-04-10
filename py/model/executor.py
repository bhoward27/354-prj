import mysql.connector
from pathlib import Path
from os import chdir

class Executor:
    '''This class provides basic functionality (insert, delete, executeFile) for executing SQL statements.'''
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.passwd = "password"
        self.database = "project"

        try:
            self.db = self.connectToDatabase()

        # This error will arise if the database "project" does not yet exist.
        except mysql.connector.errors.ProgrammingError:
            self.db = mysql.connector.connect(
                host = self.host,
                user = self.user,
                passwd = self.passwd,
                # Since "project" does not yet exist, don't specify it when connecting.
                # Note that this limits the capabilities of Executor to only being able to use
                # the executeFile method. If need to use Executor's other methods, one must
                # create the project database, then instantiate (or re-instantiate) the executor.
            )
            self.cursor = self.db.cursor()
        else:
            self.cursor = self.db.cursor()
            self.__setValidTableNames()

    def __del__(self):
        self.cursor.close()
        self.db.disconnect()
    
    def connectToDatabase(self):
        '''Returns a MySQL cursor.'''   # With the cursor, any sql statement can be executed.
        return mysql.connector.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            database = self.database,
        )
    
    def __setValidTableNames(self):
        # Note that if a table is dropped or deleted after the executor was instantiated, it won't
        # be reflected in self.validTableNames.

        self.validTableNames = []
        self.cursor.execute("SHOW TABLES;")
        results = self.cursor.fetchall()
        for result in results:
            self.validTableNames.append(result[0].lower())

    def __validateTableName(self, tableName):
        if not self.isValidTableName(tableName):
            print("ValueError: tableName '" + tableName + "' is invalid.")
            raise ValueError

    def __validateRecordType(self, record):
        if not isinstance(record, tuple) or self.hasTuple(record):
            print("TypeError: record = ", record, ", but needs to be a flat tuple.", sep = "")
            raise TypeError

    def __validateValuesType(self, values):
        if not (isinstance(values, tuple) or isinstance(values, list)):
            print("TypeError: values must be a tuple, list of tuples, or tuple of tuples.")
            raise TypeError

    def insert(self, tableName, values):
        '''Inserts the tuple(s) "values" into the table "tableName".'''
        self.__validateTableName(tableName)
        self.__validateValuesType(values)

        if self.hasTuple(values):
            for record in values:
                self.__insert(tableName, record)
            self.db.commit()
        else:
            self.__insert(tableName, values)
            self.db.commit()

    def __insert(self, tableName, record):
        '''Inserts the single tuple "record" into the table "tableName".'''
        self.__validateRecordType(record)

        sql = "INSERT INTO " + tableName + " VALUES ("
        numColumns = len(record)
        for i in range(1, numColumns + 1):
            sql += "%s, "
        sql = sql[: len(sql) - 2] + ");"
        self.cursor.execute(sql, record)

    def delete(self, tableName, whereCondition):
        '''Executes SQL statement of this form: DELETE FROM <tableName> <whereCondition>;'''
        self.__validateTableName(tableName)
        sql = "DELETE FROM " + tableName + " WHERE " + whereCondition + ";"
        self.cursor.execute(sql)
        self.db.commit()

    def executeFile(self, path):
        '''Executes the statements in the SQL file located at path.'''
        with open(path, 'r') as sqlFile:
            results = self.cursor.execute(sqlFile.read(), multi = True)

            # When multi = True, one must iterate through the results to execute the queries.
            for result in results:
                pass    # Nothing needs to be "done"--just iterate through the results.
            self.db.commit()

    @staticmethod
    def hasTuple(x):
        '''Returns true if x contains one or more tuples and false otherwise.'''
        return any(isinstance(i, tuple) for i in x)

    def isValidTableName(self, tableName):
        '''Returns true iff. tableName is a table that exists in the project database.'''
        # This method will be incorrect if tables have been dropped, added, or modified after
        # the executor was instantiated.
        return tableName.lower() in self.validTableNames