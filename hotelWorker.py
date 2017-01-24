# coding=utf-8
import sqlite3
import os
import atexit
import time

# Check if DB already exists BEFORE calling the connect, since connect will create it
DBExist = os.path.isfile('cronhoteldb.db')
# Will create a connection to 'cow.db' file. If the file does not exist, it will create it
dbCon = {}
cursor = {}

if DBExist:
    dbCon = sqlite3.connect('cronhoteldb.db')
    cursor = dbCon.cursor()


def clean(parameter):
    res = time.time()
    print "clean task " + str(res)
    return res


def breakfast(parameter):
    res = time.time()
    print "breakfast task" + str(res)
    return res


def wakeup(parameter):
    res = time.time()
    print "wakeup task" + str(res)
    return res


# map the inputs to the function blocks
options = {"clean": clean,
           "breakfast": breakfast,
           "wakeup": wakeup,
}


# this class should return the time the task has been done
# check which task is about
# do the task as the assignment
# this module has a connection to db so we can get the resident name etc
def dohoteltask(taskname, parameter):
    return options[taskname](parameter)


# Define a function to be called when the interpreter terminates
def close_db():
    if DBExist:
        dbCon.commit()
        dbCon.close()

# register close_db to be called when the interpreter terminates
atexit.register(close_db)

