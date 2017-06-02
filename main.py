__author__ = 'user'
import functions
import database
import cx_Oracle
from connection import con,cur

def main():

    database.make_all_tables()
    database.reset_withdrawals()
    choice = 1

    while choice != 0:

        print("--- Main Menu --- ")
        print("1. Sign Up (New Customer) ")
        print("2. Sign In (Existing Customer) ")
        print("3. Admin Sign In ")
        print("0. Quit ")

        try:
            choice = int(input())

        except:
            print("Invalid Choice")
            choice = 1
            continue

        if choice == 1:
            functions.sign_up();

        elif choice == 2:
            functions.sign_in();

        elif choice == 3:
            functions.admin_sign_in();

        elif choice == 0:
            print("Application Closed")

        else:
            print("Invalid Choice")



main()