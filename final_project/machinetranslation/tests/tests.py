import unittest

from translator import english_to_french, french_to_english

class TestEngToFre(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('dog'), 'Chien')
        self.assertEqual(english_to_french('bread'), 'Pain')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        self.assertNotEqual(english_to_french('None'), '')  

class TestFreToEng(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('chien'), 'Dog')
        self.assertEqual(french_to_english('chat'), 'Cat')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertNotEqual(french_to_english('None'), '')  

unittest.main()