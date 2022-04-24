#!/usr/bin/env python3.8
from account import Account
from password import Password


        #ACCOUNT CLASS
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
def delete_account(account):
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
def exist_account(username):
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

        #PASSWORD CLASS

# Function Creating a password
def create_password(plot,password):
    passwords = Password(plot,password)
    return passwords

def save_passwords(password):
    '''
    function ro save password
    '''
    password.save_password()


def delete_password(password):
    '''
    function for delete
    '''
    password.delete_password()

def find_password(plot):
    '''
    function for finding
    '''
    return Password.find_by_plot(plot)

def exist_password(plot):
    '''
    Function that check if an password exists with that plot and return a Boolean
    '''
    return Password.password_exist(plot)

def display_passwords():
    '''
    Function that returns all the saved passwords
    '''
    return Password.display_passwords()



#calling the above Functions(Main Function)

def main():
    print('.........................................')
    print("Hello Welcome to your account list.")
    print(".......................................")
    print('Please select an option')
    
    while True:
        print(
            " 1. Login \n 2. Create Account \n 3. Display Accounts \n 4. Delete \n 5. Exit")


        option = int(input())
        if option == 1:
          print("Enter your Username")
          username = input()
          print("Enter you Password")
          password = input()
          account = find_account(username)
          if account.username == username and account.password == password:

            print(f"{username} you have looged into your account ") 
            while True:
              print("..................................")
              print(f"Hello {username}, Please reply with a number") 
              print(' 1. Save new Password \n 2. Display Saved Passwords \n 3. Delete Password \n 4. Go Back')
              login_option = int(input())
              if login_option == 1:
                  print('New plot')
                  print('........................................')

                  print('Enter Plot Name')
                  plot = input()

                  print('Enter Password')
                  password = input()

                  save_passwords(create_password(plot,password))
              elif login_option == 2:
                  if display_passwords():
                      for plot in display_passwords():
                          print(f'{plot.plot} : {plot.password}')
                  else:
                      print('Sorry,No password saved for this plot')
                      print('\n')

              elif login_option == 3:
                  print('Please enter the plot to delete')

                  plot = input()
                  if exist_password(plot):
                      remove_plot = (plot) 
                      delete_password(remove_plot)

                  else:
                      print(f'If{plot} not there,enter another plot')
              elif login_option == 4:
                  print('Byee....')
                  break
            else:
                print('Wrong username or password')

        elif option == 2:
            print('New Account')
            print(".........................................")
            print('Enter your First Name')
            first_name = input()

            print('Enter your Last Name')
            last_name = input()

            print('Enter your UserName')
            username = input()

            print('Enter your Password')
            password = input()

            save_accounts(create_account(first_name, last_name, username, password))
            print('Account has been created,Thank you.')
            while True:
                print('......................................')
                print(f"Welcome  {username} ,please reply with a number")
                print(
                    '1. Save new Password \n 2. Display Saved Passwords \n 3. Delete Password \n 4. Go Back')
                login_option = int(input())
                if login_option == 1:
                  print('New plot')
                  print('........................................')

                  print('Enter Plot Name')
                  plot = input()

                  print('Enter Password')
                  password = input()

                  save_passwords(create_password(plot,password))
                elif login_option == 2:
                  if display_passwords():
                      for plot in display_passwords():
                          print(f'{plot.plot} : {plot.password}')
                  else:
                      print('Sorry,No password saved for this plot')
                      print('\n')

                elif login_option == 3:
                  print('Please enter the plot to delete')

                  plot = input()
                  if exist_password(plot):
                      remove_plot = (plot) 
                      delete_password(remove_plot)

                  else:
                      print(f'If{plot} not there,enter another plot')
                elif login_option == 4:
                  print('Byee....')
                  break
            else:
                print('Choose Number')
                
        elif option == 1:
            if display_accounts():
                for account in display_accounts():
                    print(f'{account.username}')
            else:
                print("No such Account")

        elif option == 4:
            print('Please enter the Account to delete')
            account = input()
            if exist_account(account):
                remove_account = (account)
                delete_account(remove_account)

        elif option == 5:
            print('Thank you for your service.Bye....')
            break

if __name__ == '__main__':
       main()


