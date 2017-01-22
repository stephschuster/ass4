import sys
import sqlite3
import os
import atexit

# Check if DB already exists BEFORE calling the connect, since connect will create it
DBExist = os.path.isfile('cronhoteldb.db')
# Will create a connection to 'cow.db' file. If the file does not exist, it will create it
dbCon = sqlite3.connect('cronhoteldb.db')
cursor = dbCon.cursor()


# create the tables as assignment
# fill the tables with the info from config as an argument parameter
# if the db exists - then create - otherwise exit
def create_tables():
    if not DBExist:  # First time creating the database tables.
        cursor.execute(""" CREATE TABLE TaskTimes (TaskId  INT PRIMARY KEY NOT NULL,
                                                   DoEvery INT NOT NULL,
                                                   NumTimes INT NOT NULL)""")

        cursor.execute(""" CREATE TABLE Tasks( TaskId INT NOT NULL REFERENCES TasksTimes(TaskId),
                                               TaskName TEXT NOT NULL,
                                               Parameter INT)""")

        cursor.execute(""" CREATE TABLE Rooms ( RoomNumber INT PRIMARY KEY NOT NULL )""")

        cursor.execute(""" CREATE TABLE Residents ( RoomNumber INT NOT NULL REFERENCES Rooms(RoomNumber),
                                                    FirstName TEXT NOT NULL,
                                                    LastName TEXT NOT NULL)""")


# Define a function to be called when the interpreter terminates
def close_db():
    dbCon.commit()
    dbCon.close()

# register close_db to be called when the interpreter terminates
atexit.register(close_db)

