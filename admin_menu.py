__author__ = 'user'
from connection import con,cur
import database_admin as db_admin

def print_closed_acc_history():
    res = db_admin.get_closed_accounts()
    print("Account No \t\t\t Closed On")
    for i in range(0,len(res)):
        print(res[i][0]," \t\t\t\t ",res[i][1].strftime("%d-%b-%Y"))

def print_fd_report():
    try:
        cus_id = int(input("\nEnter customer ID : "))
    except:
        print("Invalid ID")
        return
    if db_admin.check_customer_exists(cus_id) is True:
        res = db_admin.get_fd_report(cus_id)
        if len(res) == 0:
            print("N.A.")
        else:
            print("Account No \t\t\t\t Amount \t\t\t\t Deposit Term")
            for i in range(0,len(res)):
                print(res[i][0],"   \t\t\t\t\t   ",res[i][1],"   \t\t\t\t   ",res[i][2])
    else:
        print("Customer Doesn't exist")


def print_fd_report_vis_customer():
    try:
        cus_id = int(input("\nEnter customer ID : "))
    except:
        print("Invalid ID")
        return
    if db_admin.check_customer_exists(cus_id) is True:
        if db_admin.get_fd_count(cus_id) > 0:
            res = db_admin.get_fd_report_vis_customer(cus_id)
            if len(res) == 0:
                print("N.A.")
            else:
                print("Customer ID \t\t\t\t Account No \t\t\t\t Amount \t\t\t\t Deposit Term")
                for i in range(0,len(res)):
                    print(res[i][0],"   \t\t\t\t\t\t   ",res[i][1],"   \t\t\t\t\t   ",res[i][2],"  \t\t\t\t\t  ",res[i][3])
        else:
            print("Customer doesn't have any FD Account")
    else:
        print("Customer Doesn't exist")

def print_fd_report_wrt_amount():
    try:
        amount = int(input("\nEnter an amount (in multiples of 1000) : "))
    except:
        print("Invalid Amount")
        return
    if amount > 0 and amount%1000 == 0 :
        res = db_admin.get_fd_report_wrt_amount(amount)
        if len(res) == 0:
                print("N.A.")
        else:
            print("Customer ID \t\t\t\t Account No \t\t\t\t Amount \t\t\t\t Deposit Term")
            for i in range(0,len(res)):
                print(res[i][0],"   \t\t\t\t\t\t   ",res[i][1],"   \t\t\t\t\t   ",res[i][2],"  \t\t\t\t\t  ",res[i][3])

    else:
        print("Sorry ! Invalid Amount")

def print_loan_report():
    try:
        cus_id = int(input("\nEnter customer ID : "))
    except:
        print("Invalid ID")
        return
    if db_admin.check_customer_exists(cus_id) is True:
        res = db_admin.get_loan_report(cus_id)
        if len(res) == 0:
            print("Not Availed")
        else:
            print("Account No \t\t\t\t Amount \t\t\t\t Repayment Term")
            for i in range(0,len(res)):
                print(res[i][0],"   \t\t\t\t\t   ",res[i][1],"   \t\t\t\t   ",res[i][2])
    else:
        print("Customer Doesn't exist")

def print_loan_report_vis_customer():
    try:
        cus_id = int(input("\nEnter customer ID : "))
    except:
        print("Invalid ID")
        return
    if db_admin.check_customer_exists(cus_id) is True:
        if db_admin.get_loan_count(cus_id) > 0:
            res = db_admin.get_loan_report_vis_customer(cus_id)
            if len(res) == 0:
                print("N.A.")
            else:
                print("Customer ID \t\t\t\t Account No \t\t\t\t Amount \t\t\t\t Repayment Term")
                for i in range(0,len(res)):
                    print(res[i][0],"   \t\t\t\t\t\t   ",res[i][1],"   \t\t\t\t\t   ",res[i][2],"  \t\t\t\t\t  ",res[i][3])
        else:
            print("Customer hasn't availed any loan")
    else:
        print("Customer Doesn't exist")

def print_loan_report_wrt_amount():
    try:
        amount = int(input("\nEnter an amount (in multiples of 1000) : "))
    except:
        print("Invalid Amount")
        return
    if amount > 0 and amount%1000 == 0 :
        res = db_admin.get_loan_report_wrt_amount(amount)
        if len(res) == 0:
                print("N.A.")
        else:
            print("Customer ID \t\t\t\t First Name \t\t\t\t Last Name \t\t\t\t Loan Amount")
            for i in range(0,len(res)):
                print(res[i][0],"   \t\t\t\t\t\t   ",res[i][1],"   \t\t\t\t\t   ",res[i][2],"  \t\t\t\t\t  ",res[i][3])

    else:
        print("Sorry ! Invalid Amount")

def print_loan_fd_report():
    res = db_admin.get_loan_fd_report()
    if len(res) == 0:
        print("N.A.")
    else:
        print("Customer ID \t\t\t\t First Name \t\t\t\t Last Name \t\t\t\t Sum of Loan Amounts \t\t\t\t Sum of FD Amounts")
        for i in range(0,len(res)):
            print(res[i][0],"   \t\t\t\t\t\t   ",res[i][1],"   \t\t\t\t\t   ",res[i][2],"  \t\t\t\t\t  ",res[i][3], " \t\t\t\t\t ",res[i][4])


def print_report_no_loan():
    res = db_admin.get_report_no_loan()
    if len(res) == 0:
        print("N.A.")
    else:
        print("Customer ID \t\t\t\t First Name \t\t\t\t Last Name ")
        for i in range(0,len(res)):
            print(res[i][0],"   \t\t\t\t\t\t   ",res[i][1],"   \t\t\t\t\t   ",res[i][2])

def print_report_no_fd():
    res = db_admin.get_report_no_fd()
    if len(res) == 0:
        print("N.A.")
    else:
        print("Customer ID \t\t\t\t First Name \t\t\t\t Last Name ")
        for i in range(0,len(res)):
            print(res[i][0],"   \t\t\t\t\t\t   ",res[i][1],"   \t\t\t\t\t   ",res[i][2])

def print_report_no_fd_loan():
    res = db_admin.get_report_no_fd_loan()
    if len(res) == 0:
        print("N.A.")
    else:
        print("Customer ID \t\t\t\t First Name \t\t\t\t Last Name ")
        for i in range(0,len(res)):
            print(res[i][0],"   \t\t\t\t\t\t   ",res[i][1],"   \t\t\t\t\t   ",res[i][2])