import os
import sys
import json

path_module = os.path.abspath(__file__)
path_py_padre = os.path.abspath(os.path.join(path_module, '..'))
path_project = os.path.abspath(os.path.join(path_module, '..', '..', '..'))

sys.path.insert(0, path_project)
sys.path.append(path_py_padre)
__package__ = os.path.basename(path_py_padre)

from app.py.bd import BD

bd = BD()

vehicle_id = 1

ubic_ref = bd.obtener_historial_ubicfec_por_vehicle_id(vehicle_id)
print("Historial ubicacion/fecha de la unidad con vehicle_id=", vehicle_id, ': ', json.dumps(ubic_ref, indent=4))

alcaldia = 'Cuauhtémoc'
unidades = bd.obtener_unidades_pasando_alcaldia(alcaldia)
print("Unidades que pasaron en la alcaldia %s: " % alcaldia, json.dumps(unidades, indent=4))