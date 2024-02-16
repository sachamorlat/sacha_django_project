import unittest
from fonctions import est_palindrome

class TestEstPalindrome(unittest.TestCase):

    def test_palindrome_normal(self):
        self.assertTrue(est_palindrome("kayak"))

    def test_palindrome_avec_espaces(self):
        self.assertTrue(est_palindrome("kayak radar kayak"))

    def test_non_palindrome(self):
        self.assertFalse(est_palindrome("sacha"))

    def test_palindrome_sensible_a_la_case(self):
        self.assertTrue(est_palindrome("KayAk rADar Kayak"))

    def test_palindrome_chaine_vide(self):
        self.assertTrue(est_palindrome(""))

if __name__ == '__main__':
    unittest.main()
