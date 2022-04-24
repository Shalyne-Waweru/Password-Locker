class Credentials:
  """
  Class that generates new instances of account credentials
  """

  #Create an empty array to store our created credential objects
  credentials_list = []

  #Create a constructor and pass in arguments needed to create account credentials
  def __init__(self,accountType,userName,password):

    self.accountType = accountType
    self.userName = userName
    self.password = password

  #SAVING THE CREDENTIALS TO THE CREDENTIALS_LIST
  def save_credentials(self):
    """
    save_credentials method saves credential objects into the credentials_list 
    """

    Credentials.credentials_list.append(self)

  #DISPLAY THE CREDENTIALS IN THE CREDENTIALS_LIST
  @classmethod
  def display_credentials(cls):
    """
    display_credentials method returns the saved credential objects in the credentials_list 
    """

    return cls.credentials_list