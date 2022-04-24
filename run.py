#!/usr/bin/env python3.6
from user import User

def function():
	print("               ____                          _                           _                        ")
	print("              |  _ \                        | |                         | |   _                   ")
	print("              | |_) )  ____   ___   ___     | |         _____    _ _ _  | | / /    ____    _ _    ")
	print("              |  __/  / _  | / __  / __     | |        /  _  \  |  _ _) | |/ /    / __ \  | '_|   ")
	print("              | |    / (_| | \__ \ \__ \    | |_ _ _  (  (_)  ) | |_ _  | | \ \  |  ___/  | |     ")
	print("              |_|    \_____|  ___/  ___/    |_ _ _ _)  \_____/  |_ _ _) |_|  \_\  \____/  | |     ")

function()

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
  Function to create a new user
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
      print("             Enter a valid input \n")

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
      while True:
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
              print('\n')

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