import sqlite3

from .descarga_ubicacion_metrobus import generador_descarga_ubicacion_metrobus
from .limite_alcadia import obtener_poligonos_alcaldias_desde_excel
from .point_in_polygon import is_inside_sm
from .bd import (
    BD,
    query_insert_registros
)
from . import config as cnf


class ObtencionUbicacionMetrobus:
    COLUMNAS_UBICMETRO = (
        "id",
        "date_updated",
        "vehicle_id",
        "vehicle_label",
        "vehicle_current_status",
        "position_latitude",
        "position_longitude",
        "geographic_point",
        "position_speed",
        "position_odometer",
        "trip_schedule_relationship",
        "trip_id",
        "trip_start_date",
        "trip_route_id",
        "alcaldia",
    )

    def __init__(self):
        self.bd = BD()

    def ejecutar(self, chunksize=100):
        rel_alcal_polig = self.obtener_poligonos_alcaldias_desde_excel()

        count_salvados = 0
        count_fallidos = 0

        for total, records_ubicacion in self.generador_consultar_ubicacion(chunksize):
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

            is_save = self.salvar_records_a_bd(records_ubicacion)

            if not is_save:
                count_fallidos += len(records_ubicacion)
            else:
                count_salvados += len(records_ubicacion)

        return count_salvados, count_fallidos

    @staticmethod
    def generador_consultar_ubicacion(chunksize=100):
        return generador_descarga_ubicacion_metrobus(chunksize=chunksize)

    @staticmethod
    def obtener_poligonos_alcaldias_desde_excel():
        return obtener_poligonos_alcaldias_desde_excel()

    @staticmethod
    def coordenada_esta_dentrodel_poligono(poligono, coordenada):
        return is_inside_sm(poligono, coordenada)

    def salvar_records_a_bd(self, records):
        records_insert = [[
            r["id"],
            r["date_updated"],
            r["vehicle_id"],
            r["vehicle_label"],
            r["vehicle_current_status"],
            r["position_latitude"],
            r["position_longitude"],
            r["geographic_point"],
            r["position_speed"],
            r["position_odometer"],
            r["trip_schedule_relationship"],
            r["trip_id"],
            r["trip_start_date"],
            r["trip_route_id"],
            r["alcaldia"],
        ] for r in records]
        
        sql = query_insert_registros(cnf.TABLA_UBICMETRO, registros=records_insert, columnas=self.COLUMNAS_UBICMETRO)
        
        try:
            self.bd.execute(sql)
            return True
        except sqlite3.Error:
            return False
