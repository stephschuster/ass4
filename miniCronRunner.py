# coding=utf-8
import sqlite3
import os
import atexit

# Check if DB already exists BEFORE calling the connect, since connect will create it
DBExist = os.path.isfile('cronhoteldb.db')
# Will create a connection to 'cow.db' file. If the file does not exist, it will create it
dbCon = sqlite3.connect('cronhoteldb.db')
cursor = dbCon.cursor()

# do while until a db doesnt exists, there is no tasks with times > 0
# get the task with times > 0 -
# check if the task was already run in the past and check if we wait enough time
# call hotelWorker with the info (𝑑𝑜ℎ𝑜𝑡𝑒𝑙𝑡𝑎𝑠𝑘(𝑡𝑎𝑠𝑘𝑛𝑎𝑚𝑒, 𝑝𝑎𝑟𝑎𝑚𝑒𝑡𝑒𝑟)) which returns the time
# save the last time of the task
# update the task - decrease the times
# out of while - close the db


def read_task_times():
    return ""


def read_tasks():
    return ""


def update_task_times():
    return ""


# Define a function to be called when the interpreter terminates
def close_db():
    dbCon.commit()
    dbCon.close()

# register close_db to be called when the interpreter terminates
atexit.register(close_db)

