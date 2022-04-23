

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