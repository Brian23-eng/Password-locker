import unittest #Importing the unnittest module
from credentials import Credential #Importing the credentials class

class TestCredential(unittest.TestCase):

    '''
    Args:
        unittest.TestCase class that helps in creating test cases.

    '''

    def setUp(self):

        '''
        Set up method to run before each test cases

        '''
        self.new_cred = Credential('twitter', 'brian__jibril', 'steph')

    def tearDown(self):

        '''
        Method that does clean up after each test has run.

        '''
        Credential.cred_list = []

    