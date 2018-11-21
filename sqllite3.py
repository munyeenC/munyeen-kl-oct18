# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:33:17 2018

@author: munyeen.chong
"""

import sqlite3 as lite
import sys
con = None
try:
    con = lite.connect('data/testdb.db')
    cur = con.cursor()
    #cur.execute('SELECT SQLITE_VERSION()')
    cur.execute('SELECT * from stuff')
    #data = cur.fetchone()
    #print (f'SQLite version: {data}')
    
    data = cur.fetchall()
    
except lite.Error as e:
    print (f"Error {e.args[0]}")
finally :
    if con:
        con.close()