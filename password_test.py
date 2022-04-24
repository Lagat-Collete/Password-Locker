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


  if __name__ == '__main__':
    unittest.main()