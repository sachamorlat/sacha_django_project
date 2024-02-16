import unittest
from fonctions import est_premier

class TestEstPremier(unittest.TestCase):

    def test_nombre_negatif(self):
        self.assertFalse(est_premier(-5))

    def test_nombre_zero(self):
        self.assertFalse(est_premier(0))

    def test_nombre_un(self):
        self.assertFalse(est_premier(1))

    def test_nombre_petit_non_premier(self):
        self.assertFalse(est_premier(4))

    def test_nombre_petit_premier(self):
        self.assertTrue(est_premier(2))

    def test_nombre_moyen_non_premier(self):
        self.assertFalse(est_premier(10))

    def test_nombre_moyen_premier(self):
        self.assertTrue(est_premier(13))

    def test_nombre_grand_non_premier(self):
        self.assertFalse(est_premier(100))

    def test_nombre_grand_premier(self):
        self.assertTrue(est_premier(97))

    def test_nombre_tres_grand_non_premier(self):
        self.assertFalse(est_premier(1000))

    def test_nombre_tres_grand_premier(self):
        self.assertTrue(est_premier(997))

    def test_nombre_premier_trois_chiffres(self):
        self.assertTrue(est_premier(101))

    def test_nombre_non_premier_trois_chiffres(self):
        self.assertFalse(est_premier(102))

    def test_nombre_premier_negatif(self):
        self.assertFalse(est_premier(-7))

if __name__ == '__main__':
    unittest.main()
