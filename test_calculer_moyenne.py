import unittest
from fonctions import calculer_moyenne

class TestCalculerMoyenne(unittest.TestCase):
    def test_liste_non_vide(self):
        self.assertEqual(calculer_moyenne([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculer_moyenne([-1, 0, 1]), 0.0)
        self.assertEqual(calculer_moyenne([10, 20, 30, 40, 50]), 30.0)

    def test_liste_vide(self):
        self.assertEqual(calculer_moyenne([]), 0)

    def test_un_seul_element(self):
        self.assertEqual(calculer_moyenne([7]), 7.0)

    def test_liste_de_zeros(self):
        self.assertEqual(calculer_moyenne([0, 0, 0, 0]), 0.0)

    def test_liste_decimales(self):
        self.assertAlmostEqual(calculer_moyenne([1.5, 2.5, 3.5]), 2.5)

if __name__ == '__main__':
    unittest.main()
