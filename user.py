class User:
  """
  Class that generates new instances of users
  Aunthenticates a user to log in to their account
  """

  #Create an empty array to store our created user objects
  user_list = []

  #Create a constructor and pass in arguments needed to authenticate a user
  def __init__(self,userName,password):

    self.userName = userName
    self.password = password
      
  #SAVING THE USER TO THE USER_LIST
  def save_user(self):
    """
    save_user method saves user objects into the user_list 
    """

    User.user_list.append(self)

  #DISPLAY THE USERS IN THE USER_LIST
  @classmethod
  def display_users(cls):
    """
    display_users method returns the saved user objects in the user_list 
    """

    return cls.user_list

  #VERIFY A USER EXISTS IN THE USER_LIST
  @classmethod
  def verify_user(cls,userName):
      '''
      Method that checks if a user exists from the user_list.
      '''
      for user in cls.user_list:
          if user.userName == userName:
                  return True

      return False