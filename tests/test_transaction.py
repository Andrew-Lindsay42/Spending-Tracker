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

    def test_can_update_amount(self):
        self.transaction.update_amount(2.00)
        self.assertEqual(2.00, self.transaction.amount)

    def test_can_update_date(self):
        self.transaction.update_date(datetime.date(2000, 1, 1))
        self.assertEqual(datetime.date(2000, 1, 1), self.transaction.date)

    def test_can_update_description(self):
        self.transaction.update_description('Sandwich')
        self.assertEqual('Sandwich', self.transaction.description)

    def test_can_update_merchant(self):
        merchant = Merchant('Tesco', True)
        self.transaction.update_merchant(merchant)
        self.assertEqual('Tesco', self.transaction.merchant.name)

    def test_can_update_tag(self):
        tag = Tag('Groceries', True)
        self.transaction.update_tag(tag)
        self.assertEqual('Groceries', self.transaction.tag.name)