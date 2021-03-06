import unittest  # Importing the unnitest module
from account import Account  # importing the account class
# import pyperclip


class TestAccount(unittest.TestCase):
    '''
    Test class that defines test cases for the account class behaviours.

    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''
# First test -to test if our objects are being instantiated correctly.

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account(
            "Collete", "Mine", "colletemine", "mine1")  # create account object

    def test_init(self):
        '''    
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name, "Collete")
        self.assertEqual(self.new_account.last_name, "Mine")
        self.assertEqual(self.new_account.username, "colletemine")
        self.assertEqual(self.new_account.password, "mine1")

#tearDown() method
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Account.accounts_list = []

# second test- to test if the account is save into accounts_list
    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into the accounts list
        '''
        self.new_account.save_account()  # saving new account
        self.assertEqual(len(Account.accounts_list), 1)

      # Third test-to test if we can save multiple accounts
    def test_save_multiple_accounts(self):
        '''
        test_save_multiple_account to check if we can save multiple account objects to our accounts_list
        '''
        self.new_account.save_account()
        test_account = Account(
            "Collete", "Mine", "colletemine", "mine1")  # new account
        test_account.save_account()
        self.assertEqual(len(Account.accounts_list), 2)

     #Fourth test-test for delete
    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove an account from our accounts list
        '''
        self.new_account.save_account()
        test_account = Account("Collete", "Mine", "colletemine", "mine1") #new account
        test_account.save_account()

        self.new_account.delete_account() #Deleting account object
        self.assertEqual(len(Account.accounts_list),1)

        #Fifth test-for testing if we can find an account
    def test_find_account_by_username(self):
        '''
        test to check if we can find an account by username and display information
        '''
        self.new_account.save_account()
        test_account = Account("Collete", "Mine", "colletemine", "mine1") #new account
        
        test_account.save_account()
        
        found_account = Account.find_by_username("colletemine")
        self.assertEqual(found_account.username, test_account.username)

     #sixth test-test existence of an account
    def test_account_exists(self):
        '''
        Test to check if the account exist in the accounts list
        '''
        self.new_account.save_account()
        test_account = Account("Collete", "Mine", "colletemine", "mine1")
        test_account.save_account()

        account_exists = Account.account_exist('colletemine')
        self.assertTrue(account_exists)

    #seventh test- test display of the accounts 
    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''
        self.assertEqual(Account.display_accounts(),
        Account.accounts_list)

    # #Eight test
    # def test_copy_username(self):
    #   '''
    #   Test to confirm that we are copying the username from found account
    #   '''

    #   self.new_account.save_account()
    #   Account.copy_username("colletemine")

    #   self.assertEqual(self.new_account.username,pyperclip())


if __name__ == '__main__':
    unittest.main()


