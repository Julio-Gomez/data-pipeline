import os

path_module = os.path.abspath(__file__)
path_parent = os.path.dirname(path_module)
path_project = os.path.abspath(os.path.join(path_parent, '..'))

path_files = os.path.join(path_project, 'files')
path_bd = os.path.join(path_project, 'bd', 'data_pipeline.db')

path_limite_alcaldias = os.path.join(path_files, 'limite-de-las-alcaldias.csv')

ALCALDIA_NO_ENCONTRADO = 'No encontrada'
CHUNKSIZE_DEFAULT_RECORDS_UBICACION_METROBUS = 100
URL_ROOT_DATOS_CDMX = 'https://datos.cdmx.gob.mx'

TABLA_UBICMETRO = "ubicmetro"