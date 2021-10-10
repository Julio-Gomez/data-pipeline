import requests
import json


class ExceptionConsultaUbicacionMetrobus(Exception):
    pass


class ObtencionUbicacionMetrobus:
    def __init__(self):
        pass

    @staticmethod
    def generador_consultar_ubicacion(chunksize=100):
        url_root = 'https://datos.cdmx.gob.mx'

        total_records_consultados = 0

        url = (
                url_root +
                f'/api/3/action/datastore_search?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit={chunksize}')

        while True:
            resp = requests.get(url)

            if resp.status_code != 200:
                raise ExceptionConsultaUbicacionMetrobus(
                    f'La respuesta del URL {url} presenta estatus {resp.status_code}')

            resp_content = json.loads(resp.text)

            result = resp_content['result']
            links = result['_links']

            total = result['total']

            records = result['records']

            total_records_consultados += len(records)

            yield records

            if total_records_consultados == total:
                break
            else:
                url = url_root + links['next']

    def ejecutar(self, chunksize=100):
        for records_ubicacion in self.generador_consultar_ubicacion(chunksize):
            pass


ObtencionUbicacionMetrobus().ejecutar()
