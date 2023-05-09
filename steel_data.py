import os
import sqlite3

basedir = __file__.rsplit(os.sep,maxsplit=1)[0]

def connect_steel_data():
    return sqlite3.connect(f"{basedir}{os.sep}steel-data.sql")