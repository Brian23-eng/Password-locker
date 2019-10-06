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

    if User.user_exists(username):
        for user in User.user_list:
            if username == user.username and password == user.password:
                return True
            else:
                print("Invalid user name or password! Please try again.")
                # login_user()
    else:
        print("User does not exist")
        anykey = input('Kindly press any key to continue...')
        return False
    

def create_credentials(account_name, username, password):
    
    '''
        Method that create new credentials
    '''
    save_credentials(Credential(account_name, username, password))


def save_credentials(cred):
    
    '''
        Method that stores existing credentials
    '''
    Credential.cred_list.append(cred)


def display_credentials():
    
    '''
        Method that displays all credentials
    '''
    return Credential.cred_list

def generate_password(length):
    
    '''
        Method that generates passwords.
    '''
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    password = ''
    for chars in range(length):
        password += random.choice(chars)
    return password

def main():
    
    '''
    The main function that runs  before other functions
    '''

if __name__ == '__main__':
    main()





