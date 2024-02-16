import unittest
from fonctions import compter_mots

class TestCompterMots(unittest.TestCase):
    
    def test_phrase_vide(self):
        self.assertEqual(compter_mots(""), 0)
    
    def test_phrase_avec_espaces_supplementaires(self):
        self.assertEqual(compter_mots("    Ceci    est   un    test    "), 4)
    
    def test_phrase_normale(self):
        self.assertEqual(compter_mots("Bonjour je suis Sacha."), 4)
    
    def test_phrase_caracteres_speciaux(self):
        self.assertEqual(compter_mots("!@#$%^&*()"), 0)
    
    def test_phrase_avec_nombres(self):
        self.assertEqual(compter_mots("Il y a 10 redbull dans mon frigo."), 8)
    
    def test_phrase_avec_caracteres_speciaux_et_mots(self):
        self.assertEqual(compter_mots("Le prix est de 90€ par personne."), 7)
    
    def test_phrase_avec_mots_accentues(self):
        self.assertEqual(compter_mots("Fanta est une boisson très sucrée !"), 6)
    
    def test_mots_avec_apostrophes(self):
        self.assertEqual(compter_mots("C'est un test d'apostrophes."), 6)

    def test_mots_avec_tirets(self):
        self.assertEqual(compter_mots('Vingt-et-un est un nombre.'), 6)

if __name__ == '__main__':
    unittest.main()