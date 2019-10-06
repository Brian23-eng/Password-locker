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

    