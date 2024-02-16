import unittest
from fonctions import CompteBancaire

class TestCompteBancaire(unittest.TestCase):
    #Tests pour déposer 
    def test_deposer(self):
        compte = CompteBancaire(100)
        compte.deposer(50)
        self.assertEqual(compte.obtenir_solde(), 150)

    def test_deposer_zero(self):
        compte = CompteBancaire(100)
        compte.deposer(0)
        self.assertEqual(compte.obtenir_solde(), 100)

    #Tests pour retirer 
    def test_retirer(self):
        compte = CompteBancaire(100)
        compte.retirer(50)
        self.assertEqual(compte.obtenir_solde(), 50)

    def test_retirer_zero(self):
        compte = CompteBancaire(100)
        compte.retirer(0)
        self.assertEqual(compte.obtenir_solde(), 100)

    def test_retirer_solde_insuffisant(self):
        compte = CompteBancaire(100)
        with self.assertRaises(ValueError):
            compte.retirer(150)

    #Tests obtenir solde 
    def test_obtenir_solde(self):
        compte = CompteBancaire(100)
        self.assertEqual(compte.obtenir_solde(), 100)

    def test_obtenir_solde_initial(self):
        compte = CompteBancaire(0)
        self.assertEqual(compte.obtenir_solde(), 0)

if __name__ == '__main__':
    unittest.main()