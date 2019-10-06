import unittest
from user import User
from credentials import Credential
import random

def register_user(f_name, l_name, u_name, password):

    '''
    Function that creates a new user

    '''

    new_user = User(f_name, l_name, u_name, password)

    new_user.save_user()

def login_user():
   
    '''
    Function that logs in the user to Password locker

    '''
    username = input("Enter your username \n")

    password = input("Enter your password \n")

    if User.user.exists(username):
        for user in User.user_list:
            if username == user.username and password == user.password:
                return True
            
            else:
                print("Invalid username or password! Please try again")

                #login_user()

    else:
        print("User does not exist")
        clear = input("Kindly press any key to continue...")
        return False

if __name__ == '__main__':
    # main()



