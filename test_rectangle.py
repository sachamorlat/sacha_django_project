import unittest
from fonctions import Rectangle

class TestRectangle(unittest.TestCase):

    def test_calculer_perimetre(self):
        rectangle = Rectangle(5, 4)
        self.assertEqual(rectangle.calculer_perimetre(), 18)

    def test_calculer_surface(self):
        rectangle = Rectangle(5, 4)
        self.assertEqual(rectangle.calculer_surface(), 20)

    def test_calculer_perimetre_dimensions_nulles(self):
        rectangle = Rectangle(0, 0)
        self.assertEqual(rectangle.calculer_perimetre(), 0)

    def test_calculer_surface_dimensions_nulles(self):
        rectangle = Rectangle(0, 0)
        self.assertEqual(rectangle.calculer_surface(), 0)

    def test_calculer_perimetre_dimensions_egales(self):
        rectangle = Rectangle(3, 3)
        self.assertEqual(rectangle.calculer_perimetre(), 12)

    def test_calculer_surface_dimensions_egales(self):
        rectangle = Rectangle(3, 3)
        self.assertEqual(rectangle.calculer_surface(), 9)

    def test_calculer_perimetre_dimensions_decimales(self):
        rectangle = Rectangle(2.5, 3.5)
        self.assertEqual(rectangle.calculer_perimetre(), 12)

    def test_calculer_surface_dimensions_decimales(self):
        rectangle = Rectangle(2.5, 3.5)
        self.assertAlmostEqual(rectangle.calculer_surface(), 8.75, places=2)

if __name__ == '__main__':
    unittest.main()
