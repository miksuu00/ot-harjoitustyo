import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self,):
        self.userr = User("Sauli","Klonkku456")
    def test_return_right_user(self):
        self.assertEqual(("Sauli","Klonkku456"), self.userr.return_user())
