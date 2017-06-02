__author__ = 'user'
from connection import con,cur
import datetime

#sql = "select months_between(opened_on,sysdate+35) from accounts where account_no = 2"
sql = "select add_months(sysdate,1) from dual"
cur.execute(sql)
res = cur.fetchall()
#date = res[0][0].strftime("%d-%b-%Y")
aa = res[0][0].strftime("%d-%b-%Y")
print(aa)
#print(date)
#curr_date = datetime.datetime.now().strftime("%d-%b-%Y")
#print(curr_date-date)