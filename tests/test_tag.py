import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag('Groceries', True)
    
    def test_tag_id_starts_None(self):
        self.assertEqual(None, self.tag.id)    
        
    def test_tag_icon_num_starts_0(self):
        self.assertEqual(0, self.tag.icon_num)
    
    def test_tag_has_name(self):
        self.assertEqual('Groceries', self.tag.name)

    def test_tag_has_active_status(self):
        self.assertEqual(True, self.tag.active)
        self.assertNotEqual(False, self.tag.active)