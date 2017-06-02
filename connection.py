__author__ = 'user'

import cx_Oracle

con = cx_Oracle.connect("proj/mitul@localhost/xe")
cur = con.cursor()