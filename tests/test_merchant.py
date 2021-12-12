import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):
    
    def setUp(self):
        self.merchant = Merchant('Tesco', True)
    
    def test_merchant_id_starts_None(self):
        self.assertEqual(None, self.merchant.id)    
        
    def test_merchant_icon_num_starts_0(self):
        self.assertEqual(0, self.merchant.icon_num)
    
    def test_merchant_has_name(self):
        self.assertEqual('Tesco', self.merchant.name)

    def test_merchant_has_active_status(self):
        self.assertEqual(True, self.merchant.active)
        self.assertNotEqual(False, self.merchant.active)

    def test_merchant_can_update_status(self):
        self.merchant.update_status(False)
        self.assertEqual(False, self.merchant.active)
        self.assertNotEqual(True, self.merchant.active)

    def test_merchant_can_update_icon(self):
        self.merchant.update_icon(17)
        self.assertEqual(17, self.merchant.icon_num)