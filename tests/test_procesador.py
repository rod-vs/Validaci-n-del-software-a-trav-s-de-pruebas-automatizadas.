import unittest
from src.procesador import Analizador
import os

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Construir ruta absoluta al CSV, independientemente del directorio actual
        base_dir = os.path.dirname(os.path.dirname(__file__))  # Subir a la raíz del proyecto
        ruta_csv = os.path.join(base_dir, "data", "sri_ventas_2024.csv")  # Cambia el nombre del archivo si es necesario
        cls.analizador = Analizador(ruta_csv)

    # 1. Test de Exportaciones totales por mes
    def test_exportaciones_totales_por_mes(self):
        analizador = Analizador.__new__(Analizador)
        analizador.datos = [
            {"MES": "Enero", "EXPORTACIONES": "100"},
            {"MES": "Enero", "EXPORTACIONES": "200"},
            {"MES": "Febrero", "EXPORTACIONES": "300"},
        ]
        r = analizador.exportaciones_totales_por_mes()
        self.assertEqual(r["Enero"], 300)
        self.assertEqual(r["Febrero"], 300)

    # 2. Test del porcentaje de ventas con tarifa 0%
    def test_porcentaje_ventas_tarifa_0(self):
        analizador = Analizador.__new__(Analizador)
        analizador.datos = [
            {"PROVINCIA": "A", "VENTAS_NETAS_TARIFA_0": "100", "TOTAL_VENTAS": "200"},
            {"PROVINCIA": "A", "VENTAS_NETAS_TARIFA_0": "50", "TOTAL_VENTAS": "100"},
            {"PROVINCIA": "B", "VENTAS_NETAS_TARIFA_0": "200", "TOTAL_VENTAS": "400"},
        ]
        r = analizador.porcentaje_ventas_tarifa_0()
        self.assertAlmostEqual(r["A"], 50)
        self.assertAlmostEqual(r["B"], 50)

    # 3. Test de la provincia con mayor volumen de importaciones
    def test_provincia_mayor_importacion(self):
        analizador = Analizador.__new__(Analizador)
        analizador.datos = [
            {"PROVINCIA": "A", "IMPORTACIONES": "100"},
            {"PROVINCIA": "A", "IMPORTACIONES": "250"},
            {"PROVINCIA": "B", "IMPORTACIONES": "200"},
        ]
        r = analizador.provincia_mayor_importacion()
        self.assertEqual(r, "A")

if __name__ == "__main__":
    unittest.main()
