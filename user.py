class User:
  """
  Class that generates new instances of users
  Aunthenticates a user to log in to their account
  """

  #Create a constructor and pass in arguments needed to authenticate a user
  def __init__(self,userName,password):

    self.userName = userName
    self.password = password
      