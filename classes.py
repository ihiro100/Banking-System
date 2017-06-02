__author__ = 'user'

from abc import ABC,abstractmethod

class Customer():
    def set_first_name(self,fname):
        self.first_name = fname

    def set_last_name(self,lname):
        self.last_name = lname

    def set_customer_id(self,id):
        self.customer_id = id;

    def set_password(self,pwd):
        self.password = pwd

    def set_login_attempts(self,att):
        self.login_attempts = att
        if att == 0:
            self.status = "locked"

    def set_status(self,status):
        self.status = status

    def set_address(self,addr):
        self.addr = addr

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_customer_id(self):
        return self.customer_id

    def get_password(self):
        return self.password

    def get_login_attempts(self):
        return self.login_attempts

    def get_status(self):
        return self.status

    def get_addr_line1(self):
        return self.addr.line1

    def get_addr_line2(self):
        return self.addr.line2

    def get_addr_city(self):
        return self.addr.city

    def get_addr_state(self):
        return self.addr.state

    def get_addr_pincode(self):
        return self.addr.pincode


class Account(ABC):

    def set_account_no(self,acc_no):
        self.account_no = acc_no

    def set_account_type(self,type):
        self.type = type

    def set_balance(self,bal):
        self.balance = bal

    def set_withdrawals_left(self,wd):
        self.withdrawals_left = wd

    def get_account_no(self):
        return self.account_no

    def get_balance(self):
        return self.balance

    def get_account_type(self):
        return self.type

    def get_withdrawals_left(self):
        return self.withdrawals_left



class Savings(Account):

    interest = 7.5;
    min_balance = 0;

    def open_account(self,amount):
        if amount < 0:
            print("Please input a valid amount")
            return False
        else:
            self.balance = amount
            return True

    def deposit(self,amount):
        if amount < 0:
            print("Please input a valid amount");
            return False
        else:
            self.balance += amount;
            return True


    def withdraw(self,amount):
        if amount > self.balance:
            print("Sorry You don't have enough balance");
            return False
        else:
            self.balance -= amount;
            return True

class Current(Account):

    interest = 0
    min_balance = 5000

    def open_account(self,amount):
        if amount < self.min_balance:
            print("Please input a valid amount")
            return False
        else:
            self.balance = amount
            return True

    def deposit(self,amount):
        if amount < 0:
            print("Please input a valid amount");
            return False
        else:
            self.balance += amount;
            return True


    def withdraw(self,amount):
        if amount > self.balance:
            print("Sorry You don't have enough balance");
            return False
        elif self.balance - amount < 5000:
            print("Sorry You can't withdraw this much money as you need at least Rs",self.min_balance," to maintain this account")
            return False
        else:
            self.balance -= amount;
            return True


class Fixed_Deposit(Account):

    min_balance = 1000

    def open_account(self,amount):
        if amount < self.min_balance:
            print("Please input a valid amount")
            return False
        else:
            self.balance = amount
            return True

    def set_deposit_term(self,term):
        self.deposit_term = term

    def get_deposit_term(self):
        return self.deposit_term


class Address():

    def set_line_1(self,line1):
        self.line1 = line1

    def set_line_2(self,line2):
        self.line2 = line2

    def set_city(self,city):
        self.city = city

    def set_state(self,state):
        self.state = state

    def set_pincode(self,pincode):
        self.pincode = pincode