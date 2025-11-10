import csv

class Analizador:
    def __init__(self, ruta_csv):
        # Guardamos la ruta del archivo CSV
        self.ruta_csv = ruta_csv
        # Leemos el archivo CSV y guardamos los datos en memoria
        self.datos = self.leer_csv()

    def leer_csv(self):
        """Lee el archivo CSV y devuelve una lista de filas."""
        datos = []
        with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter= '|')
            for fila in lector:
                datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        """
        Devuelve un diccionario con el total de ventas por provincia.
        Ejemplo: {'Pichincha': 1000.0, 'Guayas': 2000.5}
        """
        totales = {}

        # Recorremos todas las filas del archivo
        for fila in self.datos:
            provincia = fila["PROVINCIA"]
            total_venta = float(fila["TOTAL_VENTAS"])

            # Si la provincia no está en el diccionario, la agregamos
            if provincia not in totales:
                totales[provincia] = total_venta
            else:
                # Si ya existe, sumamos el valor
                totales[provincia] += total_venta

        return totales

    def ventas_por_provincia(self, nombre):
        """
        Devuelve el total de ventas de una provincia específica.
        Ejemplo: ventas_por_provincia("Guayas") -> 2000.5
        """
        totales = self.ventas_totales_por_provincia()

        # Verificamos si la provincia está en los totales
        if nombre in totales:
            return totales[nombre]
        else:
            return 0.0