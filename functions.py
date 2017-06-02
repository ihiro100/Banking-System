__author__ = 'user'

import database
from classes import Customer,Account,Savings,Current,Address
import validate
import login_menu
import admin_menu
import database_admin as db_admin

def sign_up():

    customer = Customer()
    first_name = input("Enter First Name\n")
    last_name = input("Enter Last Name\n")
    add_line1 = input("Enter Address Line 1\n")
    add_line2 = input("Enter Address Line 2\n")
    city = input("Enter City\n")
    state = input("Enter State\n")
    try:
        pincode = int(input("Enter Pincode\n"))
        if pincode < 100000 or pincode > 999999:
            print("Invalid Pincode")
            return
    except:
        print("Invalid Pincode")
        return

    password = input("Enter password (min 8 char and max 20 char)\n")
    while len(password) < 8 or len(password) > 20:
        print("Please Enter password in given range\n")
        password = input();

    customer.set_first_name(first_name)
    customer.set_last_name(last_name)
    customer.set_password(password)
    customer.set_status("open")
    customer.set_login_attempts(3)

    addr = Address()
    addr.set_line_1(add_line1)
    addr.set_line_2(add_line2)
    addr.set_city(city)
    addr.set_state(state)
    addr.set_pincode(pincode)

    customer.set_address(addr)

    database.sign_up_customer(customer)

def sign_in():
    try:
        id = int(input("Enter Customer ID\n"))
    except:
        print("Invalid ID")
        return

    if db_admin.check_customer_exists(id) is True:
        customer = database.get_all_info_customer(id)
        if customer.get_status() == "locked":
            print("Sorry Your Account has been locked due to 3 unsuccessful login attempts")
            return
        password = input("Enter Password\n")
        res = database.login_customer(id,password)
        if res is True:
            database.reset_login_attempts(id)
            print("Login Successful")
            ch = 1
            while ch != 0:
                print("\n--- Menu ---")
                print("1. Address Change")
                print("2. Open New Account")
                print("3. Money Deposit")
                print("4. Money Withdrawal")
                print("5. Transfer Money")
                print("6. Print Statement")
                print("7. Account Closure")
                print("8. Avail Loan")
                print("0. Logout")

                try:
                    ch = int(input())
                except:
                    print("Invalid Choice")
                    ch = 1
                    continue

                if ch == 1:
                    login_menu.change_address(id)
                elif ch == 2:
                    login_menu.open_new_account(id)
                elif ch == 3:
                    login_menu.deposit_money(id)
                elif ch == 4:
                    login_menu.withdraw_money(id)
                elif ch == 5:
                    login_menu.transfer_money(id)
                elif ch == 6:
                    login_menu.print_statement(id)
                elif ch == 7:
                    login_menu.close_account(id)
                elif ch == 8:
                    login_menu.avail_loan(id)
                elif ch == 0:
                    print("Logged Out Successfully")
                else:
                    print("Invalid Choice")

        else:
            att = customer.get_login_attempts()-1
            customer.set_login_attempts(att)
            database.update_customer(customer)
            print("Incorrect Password")


    else:
        print("Customer doesn't exist")


def admin_sign_in():
    try:
        id = input("\nEnter Admin ID : ")
    except:
        print("Invalid ID")
        return

    password = input("\nEnter Password : ")
    count = 2
    res = database.login_admin(id,password)

    while count != 0 and res == False:
        print("Wrong ID or Password")
        print("Attempts Remaining : ",count)
        try:
            id = int(input("Enter Admin ID\n"))
        except:
            print("Invalid ID")
            return
        password = input("Enter Password\n")
        res = database.login_admin(id,password)
        count = count-1

    if res == True:
        print("Login Successful")
        ch = 1
        while ch != 0:
            print("\n --- Menu --- ")
            print("1. Print Closed Accounts History")
            print("2. FD report of a customer")
            print("3. FD report of a customer vis-a-vis another customer")
            print("4. FD report w.r.t a particular FD amount")
            print("5. Loan report of a customer")
            print("6. Loan report of a customer vis-a-vis another customer")
            print("7. Loan report w.r.t a particular loan amount")
            print("8. Loan - FD report of customers")
            print("9. Report of customers who are yet to avail a loan")
            print("10. Report of customers who are yet to open an FD account")
            print("11. Report of customers who neither have a loan nor an FD account with the bank")
            print("0. Admin Log Out")

            try:
                ch = int(input())
            except:
                print("Invalid Choice")
                ch = 1
                continue

            if ch == 1:
                admin_menu.print_closed_acc_history()
            elif ch == 2:
                admin_menu.print_fd_report()
            elif ch == 3:
                admin_menu.print_fd_report_vis_customer()
            elif ch == 4:
                admin_menu.print_fd_report_wrt_amount()
            elif ch == 5:
                admin_menu.print_loan_report()
            elif ch == 6:
                admin_menu.print_loan_report_vis_customer()
            elif ch == 7:
                admin_menu.print_loan_report_wrt_amount()
            elif ch == 8:
                admin_menu.print_loan_fd_report()
            elif ch == 9:
                admin_menu.print_report_no_loan()
            elif ch == 10:
                admin_menu.print_report_no_fd()
            elif ch == 11:
                admin_menu.print_report_no_fd_loan()
            elif ch == 0:
                print("Logged Out Successfully")
            else:
                print("Invalid Choice")

    else:
        print("Sorry all Attempts Finished")




