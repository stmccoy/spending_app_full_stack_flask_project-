import unittest
from src.user import User
from src.extras import *
from src.transaction import *

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.merchant_1 = Merchant("Amazon")
        self.merchant_2 = Merchant("Greggs")
        self.merchant_3 = Merchant("Farmfoods")
        self.transaction_1 = Transaction(20, "Kfc")
        self.transaction_2 = Transaction(30, "Jeans")
        self.transaction_3 = Transaction(40, "Football Match")
        self.direct_debit_1 = DirectDebit(20, "Gym")
        self.direct_debit_2 = DirectDebit(15, "Netflix")
        self.direct_debit_3 = DirectDebit(6, "Adopt a penguin")
        self.debt_1 = Debt(400, "Mortgage")
        self.debt_2 = Debt(50, "Credit card")
        self.debt_3 = Debt(100, "Student loan")
        self.user_1 = User("Steve", "Smith", 25)
        self.user_1.favourite_merchants.extend([self.merchant_1, self.merchant_2, self.merchant_3])
        self.user_1.budget = 300
        self.user_1.transactions.extend([self.transaction_1, self.transaction_2, self.transaction_3])
        self.user_1.direct_debits.extend([self.direct_debit_1, self.direct_debit_2, self.direct_debit_3])
        self.user_1.debts.extend([self.debt_1, self.debt_2, self.debt_3])
    
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
    
    def test_change_theme(self):
        self.user_1.change_theme()
        self.assertEqual(True, self.user_1.dark_mode)
    
    def test_change_theme_back(self):
        self.user_1.change_theme()
        self.user_1.change_theme()
        self.assertEqual(False, self.user_1.dark_mode)
    
    def test_age_sutability_test_pass_due_to_age(self):
        tag_1 = Tag("Gambling", True)
        self.assertEqual(True, self.user_1.age_suitability(tag_1))
    
    def test_age_sutability_test_fail_due_to_age(self):
        tag_1 = Tag("Gambling", True)
        user_2 = User("Ben", "Jones", 17)
        self.assertEqual(False, user_2.age_suitability(tag_1))
    
    def test_age_sutability_test_pass_due_to_tag_rating(self):
        tag_2 = Tag("Ice cream", False)
        user_2 = User("Ben", "Jones", 17)
        self.assertEqual(True, user_2.age_suitability(tag_2))

    