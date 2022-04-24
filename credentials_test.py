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

    #SECOND TEST
    def test_save_credentials(self):
      '''
      test_save_credentials test case to test if the credential object is being saved into the credential list
      '''

      self.new_credentials.save_credentials()

      #Check the length of our credentials_list to confirm an addition has been made to our credentials_list.
      self.assertEqual(len(Credentials.credentials_list),1) 
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            #Assign the credentials_list in the Credentials class as an empty list
            Credentials.credentials_list = []
            
    #THIRD TEST
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()

             # Create and save a new credential
            test_credential = Credentials("TestAccount","Test","Test123")
            test_credential.save_credentials()

            self.assertEqual(len(Credentials.credentials_list),2)

    #FOURTH TEST
    def test_display_credentials(self):
      '''
      test_display_credentials test case to display all the saved credentials in the credentials_list
      '''

      self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()