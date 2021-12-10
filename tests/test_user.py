import unittest
from models.user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User(123.45, 26)
    
    def test_user_id_starts_None(self):
        self.assertEqual(None, self.user.id)    
        
    def test_user_has_budget(self):
        self.assertEqual(123.45, self.user.budget)

    def test_user_has_payday(self):
        self.assertEqual(26, self.user.payday)

    def test_user_can_update_budget(self):
        self.user.update_budget(543.21)
        self.assertEqual(543.21, self.user.budget)

    def test_user_can_update_payday(self):
        self.user.update_payday(12)
        self.assertEqual(12, self.user.payday)