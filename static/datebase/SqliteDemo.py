"""
   date: 2018-03-06 22:03 
"""

__author__ = "WXGALY"

import sqlite3

connection = sqlite3.connect("test.db")

cursor = connection.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

cursor.close()

connection.commit()

connection.close()
