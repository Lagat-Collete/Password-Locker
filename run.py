#!/usr/bin/env python3.8
from pyclbr import Function

from click import option
from account import Account

# Function Creating an Account
def create_account(fname,lname,username,password):
    '''
    Function to create new account
    '''
    new_account = Account(fname,lname,username,password)
    return new_account

  #Function for saving accounts
def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()

#Function for deleting an account
def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

#Function for finding an account
def find_account(username):
    '''
    Function that finds an account by username and returns the account
    ''' 
    return Account.find_by_username(username)

#Function for checking if an account exists
def check_existing_account(username):
    '''
    Function that check if an account exists with that username and return a Boolean
    ''' 
    return Account.account_exist(username)

#Function for displaying all accounts
def display_accounts():
    '''
    Function that returns all the saved contacts
    '''
    return Account.display_accounts()

#calling the above Functions(Main Function)
def main():
    print('.........................................')
    print("Hello Welcome to your account list.")
    print(".......................................")
    print('Please select an option')
    
    while True:
        print("A.Login \n B. Create Account \n C. Display Accounts \n D. Delete \n E. Exit")


        option = int(input())
        if option == 'A':
          print("Enter your Username")
          username = input()
          print("Enter you Password")
          password = input()
          account = find_account(username)
          if account.username == username and account.password == password:

            print(f"{username} you have looged in to your account ") 
            while True:
              print("..................................")
              print 


