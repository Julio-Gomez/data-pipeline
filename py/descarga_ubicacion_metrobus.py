import requests
import json

from . import config as cnf


class ExceptionConsultaUbicacionMetrobus(Exception):
    pass


def generador_descarga_ubicacion_metrobus(chunksize=cnf.CHUNKSIZE_DEFAULT_RECORDS_UBICACION_METROBUS):
    url_root = cnf.URL_ROOT_DATOS_CDMX

    total_records_consultados = 0

    url = (
            url_root +
            f'/api/3/action/datastore_search?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit={chunksize}')

    while True:
        resp = descarga_ubicacion_metrobus(url)

        result = resp['result']
        links = result['_links']

        total = result['total']

        records = result['records']

        total_records_consultados += len(records)

        yield records

        if total_records_consultados == total:
            break
        else:
            url = url_root + links['next']


def descarga_ubicacion_metrobus(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        raise ExceptionConsultaUbicacionMetrobus(
            f'La respuesta del URL {url} presenta estatus {resp.status_code}')

    return json.loads(resp.text)
