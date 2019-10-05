import unittest
from user import User

class TestUser(unittest.TestCase):
    
    '''
     Test clas that  defines test cases foe the User class

    '''

    def setUp(self):

        '''
        Method to run before test cases

        '''
        self.new_user = User('Brian', 'Omondi', 'brian__jibril', 'steph')


if __name__ == '__main__':
    unittest.main()


