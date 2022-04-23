# import pyperclip

class Account:
    """
    Class that generates new instances of accounts.
    """

    account_list = [] # Empty account list

    def __init__(self,first_name,last_name,username,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
  
# save method
    def save_account(self):
      '''
      save_account method saves account object into account_list
      '''

      Account.account_list.append(self)

# delete method
    def delete_account(self):
      '''
      delete_account method deletes a saved account from the account_list
      '''

      Account.account_list.remove(self)

# Method for finding an account
    @classmethod
    def find_by_username(cls, username):
      '''
      Method that takes in username and return an account that matches that username.
      Args:
          username: username to serach for 
      Returns : 
          Account of a person that matches the number.
      '''

      for account in cls.account_list:
          if account.username == username:
               return account

#method for testing existence of an account
    @classmethod
    def account_exist(cls,username):
      '''
      Method that checks if an account exists from the account_list.
      Args:
          username: username to search if it exist
      Returns :
          Boolean: True or false depending if tha account exists
      '''
      for account in cls.account_list:
          if account.username == username:
              return True

          return False

#method for displaying all the accounts
    @classmethod
    def display_accounts(cls):
      '''
      method that returns the contact list
      '''
      return cls.account_list

#method  for copying
    # @classmethod
    # def copy_username(cls,username):
    #     account_found = Account.find_by_username(username)
    #     pyperclip.copy(account_found.username)

