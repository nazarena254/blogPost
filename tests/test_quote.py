import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.random_quote = Quote("Its better ro try and fail than not to try at all")
        

    def test_instance(self):
        self.assertTrue(isinstance(self.random_quote, Quote))

    def test_init(self):
        
        self.assertEqual(self.random_quote.quote,"Its better ro try and fail than not to try at all")