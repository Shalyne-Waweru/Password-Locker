# Importing the unittest module
import unittest

# Importing the Credentials class
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
      '''
      Set up method to run before each test cases.
      It defines instructions that will be executed before each test method.
      '''
      
      # Create a credential object with the accountType, userName and password arguments
      self.new_credentials = Credentials("Twitter","Shalyne","Shalyne123")

    #FIRST TEST
    def test_init(self):
      '''
      test_init test case to test if the object is initialized properly
      '''

      #The assertEqual() method checks for an expected result. 
      #The first argument is the expected result and the second argument is the result that is actually gotten. 
      self.assertEqual(self.new_credentials.accountType,"Twitter")
      self.assertEqual(self.new_credentials.userName,"Shalyne")
      self.assertEqual(self.new_credentials.password,"Shalyne123")

if __name__ == '__main__':
    unittest.main()