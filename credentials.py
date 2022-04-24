class Credentials:
  """
  Class that generates new instances of account credentials
  """

  #Create a constructor and pass in arguments needed to create account credentials
  def __init__(self,accountType,userName,password):

    self.accountType = accountType
    self.userName = userName
    self.password = password