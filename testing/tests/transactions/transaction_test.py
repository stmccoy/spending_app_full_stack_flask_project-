import unittest
from src.transactions.transaction import *


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
    
    def test_transaction_has_priority_list(self):
        self.assertEqual(3, len(self.transaction_1.priority_list))
    
    def test_transaction_has_low_priority_rating(self):
        self.transaction_1.set_priority_rating(0)
        self.assertEqual("low", self.transaction_1.priority_rating)
    
    def test_transaction_has_medium_priority_rating(self):
        self.transaction_1.set_priority_rating(1)
        self.assertEqual("medium", self.transaction_1.priority_rating)
    
    def test_transaction_has_high_priority_rating(self):
        self.transaction_1.set_priority_rating(2)
        self.assertEqual("high", self.transaction_1.priority_rating)

class TestDirectDebit(unittest.TestCase):

    def setUp(self):

        self.direct_debit_1 = DirectDebit(20, "Gasman")
    
    def test_direct_debit_has_value(self):
        self.assertEqual(20, self.direct_debit_1.value)
    
    def test_direct_debit_has_description(self):
        self.assertEqual("Gasman", self.direct_debit_1.description)
    
    def test_direct_debit_has_reoccurence_amount(self):
        self.direct_debit_1.reoccurence_frequency_amount = 1
        self.assertEqual(1, self.direct_debit_1.reoccurence_frequency_amount)
    
    def test_direct_debit_has_reoccurence_amount(self):
        self.direct_debit_1.reoccurence_frequency_amount = 1
        self.assertEqual(1, self.direct_debit_1.reoccurence_frequency_amount)
    
    def test_direct_debit_has_reoccurence_type(self):
        self.direct_debit_1.reoccurence_frequency_type = 2
        self.assertEqual(2, self.direct_debit_1.reoccurence_frequency_type)
    
    def test_direct_debit_has_reoccurence_type_amount(self):
        self.direct_debit_1.reoccurence_frequency_type_amount = 5
        self.assertEqual(5, self.direct_debit_1.reoccurence_frequency_type_amount)
    
    def test_direct_debit_has_reoccurence_type_list(self):
        self.assertEqual(3, len(self.direct_debit_1.reoccurence_frequency_type_list))

class TestDebt(unittest.TestCase):

    def setUp(self):
        self.debt_1 = Debt(10, "credit card")
    
    def test_debt_has_value(self):
        self.assertEqual(10, self.debt_1.value)
    
    def test_debt_has_description(self):
        self.assertEqual("credit card", self.debt_1.description)

    #test for inheritance from direct debit, can infer the rest is inherited from direct debit tests
    def test_debt_has_reoccurence_amount(self):
        self.debt_1.reoccurence_frequency_amount = 1
        self.assertEqual(1, self.debt_1.reoccurence_frequency_amount)
    
    def test_debt_has_interest(self):
        self.debt_1.interest = 2
        self.assertEqual(2, self.debt_1.interest)
    
    def test_debt_has_late_payment_fine(self):
        self.debt_1.late_payment_fine = 15
        self.assertEqual(15, self.debt_1.late_payment_fine)
    
    def test_debt_has_payoff_date(self):
        self.debt_1.pay_off_date = "15/11/2021"
        self.assertEqual("15/11/2021", self.debt_1.pay_off_date)