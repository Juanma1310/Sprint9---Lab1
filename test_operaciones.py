# test_operaciones.py

import unittest
from operaciones import sumar, restar, multiplicar, dividir

class TestOperacionesMatematicas(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(7, 6), 13)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(1, 1), 0)
        self.assertEqual(restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(1, 1), 1)
        self.assertEqual(dividir(-1, -1), 1)

        # Prueba para manejar el caso de dividir por cero
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()
