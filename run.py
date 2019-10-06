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
    while True:
        print("\033c")

        select = input("Welcome to the Password Locker an App developed by BranTech. Type in the following: \n \n \"login\" - to log in to you account. \n \"register\" - to create a new Password Locker Account. \n \"exist\" - to exist the Password Locker App \n \n").lower()

    print("." * 14)

    '''
    An input method that allows the user to select options when interacting with the app

    '''
    if select == 'register':
        print("\033c")
        f_name = input("Enter your first name \n")

        l_name = input("Enter your last name \n")

        u_name = input("Enter your username \n")

        password = input("Enter a desired strong password \n")
        register_user(f_name, l_name, u_name, password)
        print('\n')

        print("Your Account has been created successfully!! \n")
        
        anykey = input('Kindly press any key to continue...')
        # continue

    elif select == 'login':
        print("\033c")

        logged_in = login_user()

        while logged_in:
            print("\033c")

            print(f"Welcome. Choose:\n new - to create new credentials, \n save - to store credentials, \n display - display all credentials, \n quit - to close this section")

            selected_word = input().lower()

            if selected_word == 'new':
                print("\033c")
                account_name = input('Enter  your account name \n')
                u_name = input('Enter your user name \n')
                choice = input(
                        'Would you like to autogenerate your password?(yes/no) \n').lower()
                if choice == 'yes':
                    length = int(input('Enter password length \n'))
                    password = generate_password(length)
                else:
                     password = input('Enter password \n')

       
    













if __name__ == '__main__':
    main()





