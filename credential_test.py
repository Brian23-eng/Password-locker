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

    def test_init(self):

        '''
        test init to test if the object is initialized properly

        '''

        self.assertEqual(self.new_cred.account_name,'twitter')

        self.assertEqual(self.new_cred.username, 'brian__jibril')

        self.assertEqual(self.new_cred.password, 'steph')

    def test_save_cred(self):

        '''
        test case to check if we can save our credentilas in the empty cred_list.

        '''

        self.new_cred.save_cred()
        self.assertEqual(len(Credential.cred_list),1)

    def test_save_multiple_cred(self):

        '''
        test case to check if we can save multiple credentials objects to the cred_list

        '''
        self.new_cred.save_cred()

        test_cred = Credential('facebook', 'jesse jane', 'crew')

        test_cred.save_cred()
        self.assertEqual(len(Credential.cred_list),2)

    def test_display_cred(self):
        '''
        Test case to check if the credentials can be displayed.
        
        '''
        self.assertEqual(Credential.display_cred(), Credential.cred_list)







if __name__ == '__main__':
    unittest.main()

    