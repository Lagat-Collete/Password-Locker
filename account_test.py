import unittest # Importing the unnitest module
from account import Account # importing the account class

class TestAccount(unittest.TestCase):
  '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
#Fierst test -to test if our objects are being instantiated correctly.
  def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_account = Account("Collete","Mine","colletemine","mine1") #create account object

  def test_init(self):
      '''    
      test_init test case to test if the object is initialized properly
      '''

      self.assertEqual(self.new_account.first_name,"Collete")
      self.assertEqual(self.new_account.last_name,"Mine")
      self.assertEqual(self.new_account.username,"colletemine")
      self.assertEqual(self.new_account.password,"mine1")




























if __name__ == '__main__':
    unittest.main()
