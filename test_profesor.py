import unittest
from profesor import Profesor

class TestProfesor(unittest.TestCase):
    def test_profesor(self):
        profesor = Profesor("Pepe Cononda", "Profesor de Matemáticas", "12345")
        self.assertEqual(profesor.obtener_nombre(), "Pepe Cononda")  # Corregido el nombre aquí
        self.assertEqual(profesor.obtener_cargo(), "Profesor de Matemáticas")
        self.assertEqual(profesor.obtener_legajo(), "12345")

if __name__ == '__main__':
    unittest.main()
