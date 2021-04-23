import unittest
from src.extras import *

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant_1 = Merchant("Amazon")
        self.merchant_1.icon = "test"
        self.merchant_1.website = "www.test.com"
    
    def test_merchant_has_name(self):
        self.assertEqual("Amazon", self.merchant_1.name)
    
    def test_merchant_has_icon(self):
        self.assertEqual("test", self.merchant_1.icon)
    
    def test_merchant_has_website(self):
        self.assertEqual("www.test.com", self.merchant_1.website)

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag_1 = Tag("groceries")
        self.tag_1.adult_rating = False
        self.tag_2 = Tag("gambling")
        self.tag_2.adult_rating = True
    
    def test_tag_has_name(self):
        self.assertEqual("groceries", self.tag_1.name)
    
    def test_tag_has_adult_rating(self):
        self.assertEqual(False, self.tag_1.adult_rating)
    
    def test_tag_has_adult_rating(self):
        self.assertEqual(True, self.tag_2.adult_rating)