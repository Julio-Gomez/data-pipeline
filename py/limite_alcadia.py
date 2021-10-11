import csv
import json

from .config import path_limite_alcaldias


def obtener_poligonos_alcaldias_desde_excel():
    poligonos = {}

    with open(path_limite_alcaldias, 'r', encoding='utf-8') as file_limit_alc:
        reader = csv.DictReader(file_limit_alc)

        for row in reader:
            alcaldia = row['nomgeo']

            geo_shape = json.loads(row['geo_shape'])
            poligono = geo_shape['coordinates']

            poligonos[alcaldia] = poligono[0]

    return poligonos
