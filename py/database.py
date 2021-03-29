import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Fattest5!",
    database = "testdb",
)
my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE testdb")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# my_cursor.execute(
#     "CREATE TABLE User (name VARCHAR(255), email VARCHAR(255), age INTEGER(10),"
#     " user_id INTEGER AUTO_INCREMENT PRIMARY KEY);"
# )
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])

sql_stuff = "INSERT INTO User (name, email, age) VALUES (%s, %s, %s)"
record_1 = ("John", "john@codemy.com", 40)

my_cursor.execute(sql_stuff, record_1)
mydb.commit()