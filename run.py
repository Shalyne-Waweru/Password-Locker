#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def function():
	print("               ____                          _                           _                        ")
	print("              |  _ \                        | |                         | |   _                   ")
	print("              | |_) )  ____   ___   ___     | |         _____    _ _ _  | | / /    ____    _ _    ")
	print("              |  __/  / _  | / __  / __     | |        /  _  \  |  _ _) | |/ /    / __ \  | '_|   ")
	print("              | |    / (_| | \__ \ \__ \    | |_ _ _  (  (_)  ) | |_ _  | | \ \  |  ___/  | |     ")
	print("              |_|    \_____|  ___/  ___/    |_ _ _ _)  \_____/  |_ _ _) |_|  \_\  \____/  | |     ")

function()

#---------------------------USER FUNCTIONS -----------------------------

#1. CREATING A NEW USER
def create_user(userName,password):
  '''
  Function to create a new user
  '''
  #Creating a new user object and return it.
  new_user = User(userName,password)
  return new_user

#2. SAVING THE CREATED USER
def save_user(user):
  '''
  Function to save a created user
  '''
  user.save_user()

#3. DISPLAY THE SAVED USERS
def display_users():
  '''
  Function that returns all the saved users
  '''
  return User.display_users()

#4. VERIFYING USERS
def check_existing_users(username):
    '''
    Function that check if a user exists with that username and returns a Boolean
    '''
    return User.verify_user(username)

#5. GENERATE PASSWORD
def generate_password():
  '''
  Function that generates a random password.
  '''
  return User.generatePass()


#---------------------------CREDENTIAL FUNCTIONS -----------------------------

#1. CREATING A NEW CREDENTIAL
def create_credential(accountType,userName,password):
  '''
  Function to create a new credential
  '''
  #Creating a new credential object and return it.
  new_credential = Credentials(accountType,userName,password)
  return new_credential

#2. SAVING THE CREATED CREDENTIAL
def save_credentials(credential):
  '''
  Function to save a created credential
  '''
  credential.save_credentials()

#3. DISPLAY THE SAVED CREDENTIALS
def display_credentials():
  '''
  Function that returns all the saved credentials
  '''
  return Credentials.display_credentials()

#4. DELETE CREDENTIALS
def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

#MAIN FUNCTION
def main():
  print ('\n')
  print("                                       Welcome to PASSWORD LOCKER \n")
  print("              We Help You Manage Your Account Passwords and Generate New Passwords For You! \n")

  #---->SIGNING UP
  print("             "+"-"*20)
  print("             Create a New Account")
  print("             "+"-"*20)

  username = input("             Enter your username: ")
  print("\n")

  while True:
    print("             Use the following short codes to proceed:")
    print("             e - Enter your own password    g - Use an auto-generated password \n")

    choice = input("             Enter your choice: ").lower().strip()
    print("\n")

    if choice == 'e':
      password = input("             Enter your password: ")
      break

    elif choice == 'g':
      password = generate_password()
      print("             Password Successfully Generated!")
      break

    else:
      print("             Enter a valid input! \n")

  #Creating and saving a new user
  save_user(create_user(username,password))

  print ('\n')
  print("             Account Created Successfully!")
  print(f"             Hello {username}, your password is {password}")
  print("             "+"*"*40)
  print ('\n')

  while True:
    print("             Would you like to login to your account?:")
    print("             y - YES    n - NO \n")

    #Transform the user input to lowercase and strip any extra spaces
    choice = input("             Enter your choice: ").lower().strip()
    print("\n")


    if choice == 'y':
      #---->LOGGING IN
      print("             "+"-"*21)
      print("             Login to Your Account")
      print("             "+"-"*21)

      username = input("             Enter your username: ")

      password = input("             Enter your password: ")

      print ('\n')

      for user in display_users():
        #If user exists and entered password IS equal to the stored password
        if check_existing_users(username) and password == user.password:
            print(f"             Hello {username}.Welcome To PassWord Locker")  
            print("             "+"*"*40)
            print ('\n')
            
            #CREDENTIALS IMPLEMENTATIONS
            while True:
              print("             Use the following short codes to proceed:")
              print("             cr - Create New Account Credentials")
              print("             st - Store Existing Account Credentials")
              print("             dis - Display All Account Credentials")
              print("             del- Delete Account Credentials")
              print("             ex - EXIT") 
              print("\n")

              choice = input("             Enter your choice: ").lower().strip()
              print("\n")

              #Creating New Account Creddentials
              if choice == 'cr':
                print("             "+"-"*30)
                print("             Create New Account Credentials")
                print("             "+"-"*30)

                accountType = input("             Enter the account name: ").lower().strip()
                username = input("             Enter your username: ")
                print("\n")

                while True:
                  print("             Use the following short codes to proceed:")
                  print("             e - Enter your own password    g - Use an auto-generated password \n")

                  choice = input("             Enter your choice: ").lower().strip()
                  print("\n")

                  if choice == 'e':
                    password = input("             Enter your password: ")
                    break
                  
                  #Generating A Random Password
                  elif choice == 'g':
                    password = generate_password()
                    print("             Password Successfully Generated!")
                    break

                  else:
                    print("             Enter a valid input! \n")

                #Creating and saving a new credential
                save_credentials(create_credential(accountType,username,password))

                print ('\n')
                print("             New Account Credential Created Successfully!")
                print(f"             Account Name: {accountType}  Username: {username}  Password: {password}")
                print("             "+"*"*60)
                print ('\n')

              #Store Existing Account Credentials
              elif choice == 'st':
                print("             "+"-"*35)
                print("             Store Existing Account Credentials")
                print("             "+"-"*35)

                accountType = input("             Enter the account name: ").lower().strip()
                username = input("             Enter your account's username: ")
                password = input("             Enter your account's password: ")

                #Creating and saving a new credential
                save_credentials(create_credential(accountType,username,password))

                print ('\n')
                print("             Existing Account Credentials Stored Successfully!")
                print(f"             Account Name: {accountType}  Username: {username}  Password: {password}")
                print("             "+"*"*65)
                print ('\n')

              #Display All the Saved Account Credentials
              elif choice == 'dis':
                print("             "+"-"*31)
                print("             Display All Account Credentials")
                print("             "+"-"*31)
                print("\n")

                #If there are saved account credentials
                if display_credentials():
                  print("             Here's a list of all you account credentials:-->")
                  print("\n")

                  for account in display_credentials():
                    print(f"             Account Name: {account.accountType}")
                    print(f"             Account Username: {account.userName}")
                    print(f"             Account Password: {account.password}")
                    print("\n")

                #If there are NO saved account credentials
                else:
                  print("             You Don't have any existing account credentials")
                  print("             Login to create a new account or store your existing accounts")
                  print("             "+"*"*60)
                  print("\n")

              #Deleting Credentials
              elif choice == 'del':
                print("             "+"-"*26)
                print("             Delete Account Credentials")
                print("             "+"-"*26)
                print("\n")

                search_credential = input("             Enter the Account Name you want to Delete: ").lower().strip()
                print("\n")
                
                #If there are saved account credentials
                if display_credentials():

                  for credential in display_credentials():

                    #Check if the searched account name matches any saved account credentials
                    if search_credential == credential.accountType:
                      print("             The following credentials were found:--->")
                      print("\n")

                      print(f"             Account Name: {credential.accountType}")
                      print(f"             Account Username: {credential.userName}")
                      print(f"             Account Password: {credential.password}")
                      print("\n")

                      while True:
                        print(f"             Are you sure you want to delete {search_credential} account credentials? y/n")
                        print("\n")

                        choice = input("             Enter your choice: ").lower().strip()
                        print("\n")

                        if choice == 'y':
                          credential.delete_credential()
                          print(f"             {search_credential} Account Credentials Deleted Successfully!")
                          print("             "+"*"*50)
                          print("\n")
                          break

                        elif choice == 'n':
                          print(f"             {search_credential} Account Credentials Deletion Terminated!")
                          print("             "+"*"*50)
                          print("\n")
                          break

                        else:
                          print("             Enter a valid input! \n")
        
                    #If the searched account name DOESN'T match any saved account credentials
                    else:
                      print(f"             No {search_credential} credentials were found")
                      print("             "+"*"*34)
                      print("\n")

                #If there are NO saved account credentials
                else:
                  print("             You Don't have any existing account credentials")
                  print("             Login to create a new account or store your existing accounts")
                  print("             "+"*"*60)
                  print("\n")

              elif choice == 'ex':
                print("             Thank you for Using Password Locker")
                print("             "+"*"*40)
                print ('\n')
                break

              else:
                print("             Enter a valid input! \n")

        #If user exists and entered password is NOT equal to the stored password
        elif check_existing_users(username) and password != user.password:
          print("             Invalid password. Please try Again \n")
          break
        
        #If user DOESN'T exist
        else:
          print("             That user does not exist \n")
          break

    elif choice == 'n':
      print("             Logging Out.See You Next Time...")
      break

    else:
      print("             Enter a valid input \n")

if __name__ == '__main__':

  main()