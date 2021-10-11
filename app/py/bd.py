from py.bd import (
    BD as bd_conn,
    filtro_contenidoen
)
from py import config as cnf


TABLA_UBICMETRO = cnf.TABLA_UBICMETRO


class BD:
    def __init__(self):
        self.conn = bd_conn()

    def obtener_historial_ubicfec_por_id(self, id_):
        sql = f'''
            SELECT
                geographic_point,
                date_updated
            FROM
                {TABLA_UBICMETRO}
            WHERE
                id='{id_}'
            ORDER BY
                geographic_point,
                date_updated
        '''

        resp = self.conn.select(sql)

        return [{'geographic_point': r[0], 'date_updated': r[1]} for r in resp]

    def obtener_historial_ubicfec_por_vehicle_id(self, vehicle_id):
        sql = f'''
            SELECT
                geographic_point,
                date_updated,
                vehicle_id
            FROM
                {TABLA_UBICMETRO}
            WHERE
                vehicle_id='{vehicle_id}'
            ORDER BY
                geographic_point,
                date_updated
        '''

        resp = self.conn.select(sql)

        return [{
            'geographic_point': r[0],
            'date_updated': r[1],
            'vehicle_id': r[2]
        } for r in resp]


    def obtener_unidades_pasando_alcaldia(self, alcaldia):
        sql = f'''
            SELECT 
                id,
                vehicle_id,
                alcaldia 
            FROM 
               {TABLA_UBICMETRO}
            WHERE
                alcaldia LIKE '%{alcaldia}%'
            ORDER BY
                date_updated
        '''

        resp = self.conn.select(sql)

        return [{
            'id': r[0],
            'vehicle_id': r[1],
            'alcaldia': r[2]
        } for r in resp]
