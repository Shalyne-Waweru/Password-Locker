#!/usr/bin/env python3.6

from curses.ascii import US
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

  password = input("             Enter your password: ")

  #Creating and saving a new user
  save_user(create_user(username,password))

  print ('\n')
  print("             Account Created Successfully!")
  print(f"             Hello {username}, your password is {password}")
  print("             "+"*"*40)
  print ('\n')

if __name__ == '__main__':

  main()