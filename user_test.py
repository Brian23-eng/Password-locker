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

    def test_init(self):

        '''
        Test case to check if initialization of objects are proper

        '''

        self.assertEqual(self.new_user.first_name, 'Brian')

        self.assertEqual(self.new_user.last_name, 'Omondi')

        self.assertEqual(self.new_user.username, 'brian__jibril')
        
        self.assertEqual(self.new_user.password, 'steph')





if __name__ == '__main__':
    unittest.main()



