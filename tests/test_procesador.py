import unittest 

from src.procesador import Analizador

from pathlib import Path


class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("data/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        self.assertEqual(total_provincias, 24)

    def test_ventas_totales_mayores_5k(self):
      resumen = self.analizador.ventas_totales_por_provincia()
      bandera = True
      self.assertTrue(bandera)
      self.assertTrue(all(float(v)> 5000 for v in resumen.values()))

    def test_ventas_por_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")

    def test_ventas_por_provincia_existente(self):
        resultado = self.analizador.ventas_por_provincia("pichincha")
        self.assertGreater(resultado, 0)

if __name__ == '__main__':
    unittest.main()