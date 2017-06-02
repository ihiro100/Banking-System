__author__ = 'user'

import cx_Oracle
//you must have Oracle database userId and password for connection from database.
con = cx_Oracle.connect("userId/password@localhost/xe")
cur = con.cursor()
