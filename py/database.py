import mysql.connector
from pathlib import Path
from os import chdir
from model.executor import Executor

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "Fattest5!",
#     # database = "test_project",
# )
# my_cursor = mydb.cursor()

# # my_cursor.execute("CREATE DATABASE testdb")

# # my_cursor.execute("SHOW DATABASES")
# # for db in my_cursor:
# #     print(db)

# # my_cursor.execute(
# #     "CREATE TABLE User (name VARCHAR(255), email VARCHAR(255), age INTEGER(10),"
# #     " user_id INTEGER AUTO_INCREMENT PRIMARY KEY);"
# # )
# # my_cursor.execute("SHOW TABLES")
# # for table in my_cursor:
# #     print(table[0])

# # sql_stuff = "INSERT INTO User (name, email, age) VALUES (%s, %s, %s)"
# # record_1 = ("John", "john@codemy.com", 40)

# # my_cursor.execute(sql_stuff, record_1)
# # mydb.commit()

# # with open('sql/', 'r') as f:
# #     with mydb.cursor() as cursor:
# #         cursor.execute(f.read(), multi=True)
# #     mydb.commit()

# chdir('..')
# with open('sql/create_tables.sql', 'r') as file:
#     results = my_cursor.execute(file.read(), multi = True)
#     for result in results:
#         print("Running query:", result)
#         print(f"Affected {result.rowcount} rows" )
#     mydb.commit()

# # with open('test1.sql', 'r') as sql_file:
# #     result_iterator = cur.execute(sql_file.read(), multi=True)
# #     for res in result_iterator:
# #         print("Running query: ", res)  # Will print out a short representation of the query
# #         print(f"Affected {res.rowcount} rows" )

# #     con.commit()  # Remember to commit all your changes!

# my_cursor.execute("SHOW DATABASES")
# print("DATABASES")
# for db in my_cursor:
#     print(db[0])
# # my_cursor.execute("SHOW TABLES")
# # print("\nTABLES")
# # for table in my_cursor:
# #     print(table[0])


# my_cursor.close()

exec = Executor()

# preId = '000090005'
# records = []
# for i in range(1, 10):
#     records.append((preId + str(i), 13.99, 1, 1, None, 'Shrek', 'DreamWorks', None, None, None))

# exec.insert("Item", records)
exec.delete("Item", "item_id = '0000900047'")