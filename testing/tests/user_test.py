import unittest
from src.user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user_1 = User("Steve", "Smith", 25)
        self.user_1.favourite_merchants.extend(["test", "test", "test"])
        self.user_1.budget = 300
        self.user_1.transactions.extend(["test", "test", "test"])
        self.user_1.direct_debits.extend(["test", "test", "test"])
        self.user_1.debts.extend(["test", "test", "test"])
    
    def test_user_has_name(self):
        self.assertEqual("Steve", self.user_1.first_name)
    
    def test_user_has_surname(self):
        self.assertEqual("Smith", self.user_1.surname)
    
    def test_user_has_age(self):
        self.assertEqual(25, self.user_1.age)
    
    def test_user_has_favourite_merchants(self):
        self.assertEqual(3, len(self.user_1.favourite_merchants))
    
    def test_user_has_budget(self):
        self.assertEqual(300, self.user_1.budget)
    
    def test_user_has_transactions(self):
        self.assertEqual(3, len(self.user_1.transactions))
    
    def test_user_has_direct_debits(self):
        self.assertEqual(3, len(self.user_1.direct_debits))

    def test_user_has_a_theme_preference(self):
        self.assertEqual(False, self.user_1.dark_mode)
    
    def test_user_has_a_theme_preference(self):
        self.user_1.dark_mode = True
        self.assertEqual(True, self.user_1.dark_mode)

    def test_user_has_debts(self):
        self.assertEqual(3, len(self.user_1.debts))

    