import unittest
from entities.reference import Reference

class TestReference(unittest.TestCase):
    def setUp(self):
        self.reference = Reference()
    
    def test_constructor_works_properly(self):
        self.assertTrue(isinstance(self.reference.fields, dict))