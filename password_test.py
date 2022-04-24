import unittest # Importing the unittest module
from password import Password # Importing the password class

class TestPassword(unittest.TestCase):
  '''
  Test class that defines test cases for the password class behaviours
  Args:
      unittest.TestCase: TestCase class that helps in creating test cases
  '''

  #First test-to check if our objects are being instantiated correctly
  def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_password = Password("facebook","face1") #create password object
    
  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_password.plot,'facebook')
    self.assertEqual(self.new_password.password,'face1')

#Second Test_test saving
  def test_save_password(self):
    '''
    test_save_password test case to test if the password object is saved into the password_list
    '''
    self.new_password.save_password()  #saving the new password
    self.assertEqual(len(Password.password_list),1)
    

if __name__ == '__main__':
    unittest.main()