
import unittest
import unit_testing_overview

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = unit_testing_overview.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = unit_testing_overview.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ =='__main__':
    unittest.main()