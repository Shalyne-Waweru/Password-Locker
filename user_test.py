# Importing the unittest module
import unittest

# Importing the User class
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
      '''
      Set up method to run before each test cases.
      It defines instructions that will be executed before each test method.
      '''
      
      # Create a user object with the userName and password arguments
      self.new_user = User("Shalyne","Shalyne123")

    #FIRST TEST
    def test_init(self):
      '''
      test_init test case to test if the object is initialized properly
      '''

      #The assertEqual() method checks for an expected result. 
      #The first argument is the expected result and the second argument is the result that is actually gotten. 
      self.assertEqual(self.new_user.userName,"Shalyne")
      self.assertEqual(self.new_user.password,"Shalyne123")

    #SECOND TEST
    def test_save_user(self):
      '''
      test_save_user test case to test if the object is being saved into the user list
      '''

      self.new_user.save_user()

      #Check the length of our user_list to confirm an addition has been made to our user list.
      self.assertEqual(len(User.user_list),1)    

    #THIRD TEST
    def test_display_users(self):
      '''
      test_display_users test case to display all the saved users in the user list
      '''

      self.assertEqual(User.display_users(),User.user_list)


if __name__ == '__main__':
    unittest.main()