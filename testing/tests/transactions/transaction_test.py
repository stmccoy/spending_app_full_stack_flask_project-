import unittest
from src.transactions.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):

        self.transaction_1 = Transaction(100, "Shoes")
    
    def test_transaction_has_value(self):
        self.assertEqual(100, self.transaction_1.value)

    def test_transaction_has_description(self):
        self.assertEqual("Shoes", self.transaction_1.description)
    
    def test_transaction_has_merchant(self):
        self.transaction_1.merchant = "test"
        self.assertEqual("test", self.transaction_1.merchant)
    
    def test_transaction_has_merchant(self):
        self.transaction_1.merchant = "test"
        self.assertEqual("test", self.transaction_1.merchant)
    
    def test_transaction_has_tags(self):
        self.transaction_1.tags.extend(['test', 'test', 'test'])
        self.assertEqual(3, len(self.transaction_1.tags))
    
    def test_transaction_has_low_priority_rating(self):
        self.transaction_1.set_priority_rating(0)
        self.assertEqual("low", self.transaction_1.priority_rating)
    
    def test_transaction_has_medium_priority_rating(self):
        self.transaction_1.set_priority_rating(1)
        self.assertEqual("medium", self.transaction_1.priority_rating)
    
    def test_transaction_has_high_priority_rating(self):
        self.transaction_1.set_priority_rating(2)
        self.assertEqual("high", self.transaction_1.priority_rating)
    