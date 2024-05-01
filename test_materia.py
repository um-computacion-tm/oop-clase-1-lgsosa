import unittest
from profesor import Profesor
from materia import Materia, Alumno

class TestMateria(unittest.TestCase):
    def test_materia(self):
        profesor = Profesor("Marianela Fuseneco", "Profesora de Física", "67890")
        materia = Materia("Física Cuántica", [profesor])
        self.assertEqual(materia.obtener_profesores(), [profesor])

    def test_alumno(self):
        alumno = Alumno("Luisito Comunica ", "A123")
        self.assertEqual(alumno.obtener_nombre(), "Luisito Comunica ")
        self.assertEqual(alumno.obtener_legajo(), "A123")

    def test_materia_alumnos(self):
        materia = Materia("Programación Avanzada", [])
        alumno1 = Alumno("Pepe Argento", "B456")
        alumno2 = Alumno("Mony Argento", "C789")
        materia.obtener_alumnos().extend([alumno1, alumno2])
        self.assertEqual(materia.obtener_alumnos(), [alumno1, alumno2])

if __name__ == '__main__':
    unittest.main()
