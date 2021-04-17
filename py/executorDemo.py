# This file shows some examples of the Executor class being used.

import mysql.connector
from pathlib import Path
from os import chdir

from model.executor import Executor

THIS_FILES_FOLDER = "py"

exec = Executor()
chdir('..')
path = str(Path.cwd()) + '/sql/create_tables.sql'

# This executes the queries contained in the sql file located at path.
exec.executeFile(path)

# Return to the original working directory in case other file operations will occur later.
chdir(THIS_FILES_FOLDER)

# Re-instantiate the executor. This is done only because the create_tables.sql file creates the
# the project database. If this is the first time the code has been run, then "project" did not
# exist when exec was first instantiated--and therefore, if you, for example, try to insert a tuple,
# it will not work because it does not know which database to refer to. Therefore, in this case it
# is necessary to re-instantiate the executor.
exec = Executor()

# INSERT INTO Item ("0000000016", 13.99, 1, 1, NULL, "Shrek", "DreamWorks", "English", NULL, NULL);
isbn = "978-0-533-3754"
exec.insert("Book (ISBN13, price, title, publisher, language)", (isbn, 24.00, "Ishmael", "Bantam Books", "English"))
exec.insert("Item (bookISBN)", (isbn,))
# It is also possible to pass as the second argument a tuple of tuples or list of tuples.
# In that case, it will insert multiple records in one go.

# DELETE FROM Item WHERE item_ID = '0000000016';
# Uncomment below statement to see if it works.
# exec.delete("Item", "item_ID = '0000000016'")