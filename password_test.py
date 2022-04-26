
import unittest # Importing the unittest module
from password import Password # Importing the password class

class TestPasswords(unittest.TestCase):

  #First test-to check if our objects are being instantiated correctly
  def setUp(self):
    '''
    Test class that defines test cases for the password class behaviours
    '''
    self.new_password = Password("facebook","face1") #create password object
    
  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''

    Password.passwords_list = []


  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_password.site, 'facebook')
    self.assertEqual(self.new_password.password, '1234')

#Second Test_test saving
  def test_save_site(self):
    '''
    test_save_site test case to test if the password object is saved into the passwords_list
    '''
    self.new_password.save_site()  #saving the new password
    self.assertEqual(len(Password.passwords_list), 1)

 #Third Test-for multiple passwords
  def test_save_multiple_site(self):
    '''
    to check if we can save multiple site in the list
    '''
    self.new_password.save_site()
    test_pass = Password("wi-fi","wifi1") # new password
    test_pass.save_site()
    self.assertEqual(len(Password.passwords_list), 2)

  #Fourth Test-for delete
  def test_delete_site(self):
    '''
    test delete action
    '''
    self.new_password.save_site()
    test_pass = Password('wi-fi','wifi1')
    test_pass.save_site()
    self.new_password.delete_site()
    self.assertEqual(len(Password.passwords_list), 1)

  #Fifth-test for finding
  def test_find_site(self):
    '''
    This checks if we can find password using site name
    '''
    self.new_password.save_site()
    test_pass = Password('wi-fi','wifi1')
    test_pass.save_site()
    found_site = Password.find_by_site('wi-fi')
    self.assertEqual(found_site.site, test_pass.site)

  #sixth-Test -For existence
  def test_site_exists(self):
    '''
    returns a true/false value depending on value presence on search
    '''

    self.new_password.save_site()
    test_pass = Password('wi-fi','wifi1')
    test_pass.save_site()
    site_exist = Password.find_by_site('wi-fi')
    self.assertTrue(site_exist)


  def test_display_all_passwords(self):
        '''
        method that resturns a list of all passwords saved
        '''

        self.assertEqual(Password.display_passwords(),Password.password_list)



if __name__ == '__main__':
    unittest.main()