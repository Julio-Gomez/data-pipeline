from .descarga_ubicacion_metrobus import generador_descarga_ubicacion_metrobus
from .limite_alcadia import obtener_poligonos_alcaldias_desde_excel
from .point_in_polygon import is_inside_sm
from . import config as cnf


class ObtencionUbicacionMetrobus:
    def __init__(self):
        pass

    def ejecutar(self, chunksize=100):
        rel_alcal_polig = self.obtener_poligonos_alcaldias_desde_excel()

        for records_ubicacion in self.generador_consultar_ubicacion(chunksize):
            for record in records_ubicacion:
                latitud = record['position_latitude']
                longitud = record['position_longitude']

                alcaldias_encontrado = []
                for alcaldia, poligono in rel_alcal_polig.items():
                    estatus = is_inside_sm(poligono, (longitud, latitud))

                    if estatus == 1:
                        alcaldias_encontrado.append(alcaldia)
                        break

                    if estatus == 2:
                        alcaldias_encontrado.append(alcaldia)

                if not alcaldias_encontrado:
                    alcaldias_encontrado.append(cnf.ALCALDIA_NO_ENCONTRADO)

                record['alcaldia'] = '-'.join(alcaldias_encontrado)

                print(record)

    @staticmethod
    def generador_consultar_ubicacion(chunksize=100):
        return generador_descarga_ubicacion_metrobus(chunksize=chunksize)

    @staticmethod
    def obtener_poligonos_alcaldias_desde_excel():
        return obtener_poligonos_alcaldias_desde_excel()

    @staticmethod
    def coordenada_esta_dentrodel_poligono(poligono, coordenada):
        return is_inside_sm(poligono, coordenada)
