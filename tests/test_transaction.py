import unittest
import datetime
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction(1.00, datetime.date(2021, 12, 10))
    
    def test_transaction_id_starts_None(self):
        self.assertEqual(None, self.transaction.id)    
        
    def test_transaction_merchant_starts_None(self):
        self.assertEqual(None, self.transaction.merchant)
    
    def test_transaction_tag_starts_None(self):
        self.assertEqual(None, self.transaction.tag)

    def test_transaction_description_starts_None(self):
        self.assertEqual(None, self.transaction.description)

    def test_transaction_has_amount(self):
        self.assertEqual(1.00, self.transaction.amount)

    def test_transaction_has_date(self):
        self.assertEqual(datetime.date(2021, 12, 10), self.transaction.date)

    def test_can_create_transaction_with_description(self):
        transaction = Transaction(1.00, datetime.date(2021, 12, 10), 'Sandwich')
        self.assertEqual('Sandwich', transaction.description)

    def test_can_create_transaction_with_merchant(self):
        merchant = Merchant('Tesco', True)
        transaction = Transaction(1.00, datetime.date(2021, 12, 10), None, merchant)
        self.assertEqual('Tesco', transaction.merchant.name)

    def test_can_create_transaction_with_tag(self):
        tag = Tag('Groceries', True)
        transaction = Transaction(1.00, datetime.date(2021, 12, 10), None, None, tag)
        self.assertEqual('Groceries', transaction.tag.name)