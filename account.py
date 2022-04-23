

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
