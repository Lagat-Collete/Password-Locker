

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
    
  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''

    Password.password_list = []


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

#Third Test-for multiple passwords
  def test_save_multiple_password(self):
    '''
    test_save_multiple_password to check if we can save multiple password
            objects to our password_list

    '''
    self.new_password.save_password()
    test_pass = Password("wi-fi","wifi1") # new password
    test_pass.save_password()
    self.assertEqual(len(Password.password_list),2)

    #Fourth Test-for delete
  def test_delete_password(self):
    '''
    test delete action
    '''
    self.new_password.save_password()
    test_pass = Password('wi-fi','wifi1')
    test_pass.save_password()
    self.new_password.delete_password()
    self.assertEqual(len(Password.password_list),1)

    #Fifth-test for finding
  def test_find_password(self):
    '''
    This checks if we can find password using plot name
    '''
    self.new_password.save_password()
    test_pass = Password('wi-fi','wifi1')
    test_pass.save_password()
    found_password = Password.find_by_plot('wi-fi')
    self.assertEqual(found_password.plot, test_pass.plot)

    #sixth-Test -For existence
  def test_exists(self):
    '''
    returns a true/false value depending on value presence on search
    '''

    self.new_password.save_password()
    test_pass = Password('wi-fi','wifi1')
    test_pass.save_password()
    plot_exist = Password.find_by_plot('wi-fi')
    self.assertTrue(plot_exist)





if __name__ == '__main__':
    unittest.main()