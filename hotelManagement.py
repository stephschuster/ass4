import sys
import sqlite3
import os
import atexit

# Check if DB already exists BEFORE calling the connect, since connect will create it
DBExist = os.path.isfile('cronhoteldb.db')
# Will create a connection to 'cow.db' file. If the file does not exist, it will create it
dbCon = sqlite3.connect('cronhoteldb.db')
cursor = dbCon.cursor()

configFile = sys.argv[1]


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


def insert_data():
    content = []
    taskId = 0
    with open(configFile) as inputFile:
        content = inputFile.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    for line in content:
        taskId = decode_config_file_line(line, taskId)


def decode_config_file_line(line, taskId):
    line_fields = line.split(",")
    return options[line_fields[0]](line_fields, taskId)


def room(lineFields, taskId):
    cursor.execute("INSERT INTO Rooms VALUES (?)", [lineFields[1]])
    if len(lineFields) == 4:
        cursor.execute("INSERT INTO Residents VALUES (?, ?, ?)", [lineFields[1], lineFields[2], lineFields[3]])
    return taskId


def clean(lineFields, taskId):
    cursor.execute("INSERT INTO TaskTimes VALUES (?, ?, ?)", [taskId, lineFields[1], lineFields[2]])
    cursor.execute("INSERT INTO Tasks VALUES (?, ?, ?)", [taskId, lineFields[0], 0])
    return taskId+1


def breakfast(lineFields, taskId):
    cursor.execute("INSERT INTO TaskTimes VALUES (?, ?, ?)", [taskId, lineFields[1], lineFields[2]])
    cursor.execute("INSERT INTO Tasks VALUES (?, ?,?)", [taskId, lineFields[0], lineFields[3]])
    return taskId+1


def wakeup(lineFields, taskId):
    cursor.execute("INSERT INTO TaskTimes VALUES (?, ?, ?)", [taskId, lineFields[1], lineFields[2]])
    cursor.execute("INSERT INTO Tasks VALUES (?, ?, ?)", [taskId, lineFields[0], lineFields[3]])
    return taskId + 1

# map the inputs to the function blocks
options = {"room": room,
           "clean": clean,
           "breakfast": breakfast,
           "wakeup": wakeup,
}


# Define a function to be called when the interpreter terminates
def close_db():
    dbCon.commit()
    dbCon.close()


def main():
    if not DBExist:
        create_tables()
        insert_data()


if __name__ == '__main__':
    main()

# register close_db to be called when the interpreter terminates
atexit.register(close_db)

