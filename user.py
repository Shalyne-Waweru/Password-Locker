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
      
  #Saving the user to the user_list
  def save_user(self):
    """
    save_user method saves user objects into the user_list 
    """

    User.user_list.append(self)