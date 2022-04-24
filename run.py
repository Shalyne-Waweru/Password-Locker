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
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.del_credential()


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

              if choice == 'cr':
                print("             "+"-"*30)
                print("             Create New Account Credentials")
                print("             "+"-"*30)

                accountType = input("             Enter the account name: ")
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

                #Creating and saving a new credential
                save_credentials(create_credential(accountType,username,password))

                print ('\n')
                print("             New Account Credential Created Successfully!")
                print(f"             Hello {username}, your {accountType}'s password is {password}")
                print("             "+"*"*50)
                print ('\n')
                break

              elif choice == 'st':
                print("             "+"-"*30)
                print("             Store Existing Account Credentials")
                print("             "+"-"*30)

                accountType = input("             Enter the account name: ")
                username = input("             Enter your account's username: ")
                password = input("             Enter your account's password: ")

                #Creating and saving a new credential
                save_credentials(create_credential(accountType,username,password))

                print ('\n')
                print("             Existing Account Credentials Stored Successfully!")
                print(f"             Account Name: {accountType}  Username: {username}  Password: {password}")
                print("             "+"*"*65)
                print ('\n')

                break

              elif choice == 'dis':
                print("             "+"-"*31)
                print("             Display All Account Credentials")
                print("             "+"-"*31)
                print("\n")

                break

              elif choice == 'del':
                print("             "+"-"*30)
                print("             Delete Account Credentials")
                print("             "+"-"*30)
                break

              elif choice == 'ex':
                print("             Thank you for Using Password Locker")
                print("             "+"*"*40)
                print ('\n')
                break

              else:
                print("             Enter a valid input! \n")
                break

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