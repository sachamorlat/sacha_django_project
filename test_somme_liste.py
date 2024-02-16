import unittest

def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

class TestSommeListe(unittest.TestCase):

    def test_somme_liste_vide(self):
        resultat = somme_liste([])
        self.assertEqual(resultat, 0)

    def test_somme_liste_elements_positifs(self):
        resultat = somme_liste([1, 2, 3, 4, 5])
        self.assertEqual(resultat, 15)

    def test_somme_liste_elements_negatifs(self):
        resultat = somme_liste([-1, -2, -3, -4, -5])
        self.assertEqual(resultat, -15)

    def test_somme_liste_melange_elements(self):
        resultat = somme_liste([1, -2, 3, -4, 5])
        self.assertEqual(resultat, 3)

    def test_somme_liste_un_seul_element(self):
        resultat = somme_liste([42])
        self.assertEqual(resultat, 42)

    def test_somme_liste_nombres_decimaux(self):
        resultat = somme_liste([1.5, 2.5, 3.5])
        self.assertEqual(resultat, 7.5)

    def test_somme_liste_elements_non_numeriques(self):
        with self.assertRaises(TypeError):
            somme_liste(['a', 'b', 'c'])

    def test_somme_liste_elements_none(self):
        with self.assertRaises(TypeError):
            somme_liste([None, None, None])

    def test_somme_liste_elements_different_types_numeriques(self):
        resultat = somme_liste([1, 2.5, 3.7])
        self.assertEqual(resultat, 7.2)

if __name__ == '__main__':
    unittest.main()