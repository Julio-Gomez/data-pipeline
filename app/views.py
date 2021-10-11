from app import app
from app.py.bd import BD

from flask import jsonify


@app.route('/unidades/<disponibles>', methods=('GET',))
def unidades_disponibles(disponibles):
   pass


@app.route('/ubicaciones-fechas/<vehicle_id>', methods=('GET',))
def historial_ubicfec_por_id(vehicle_id):
   bd = BD()

   historial = bd.obtener_historial_ubicfec_por_vehicle_id(vehicle_id)

   return jsonify({'Status': 'OK', 'Total': len(historial), 'Records': historial})


@app.route('/alcaldias/<disponibles>', methods=('GET',))
def alcaldias_disponibles(id):
   pass


@app.route('/unidades/pasando-alcaldia/<alcaldia>', methods=('GET',))
def unidades_pasando_alcadia(alcaldia):
   bd = BD()

   unidades = bd.obtener_unidades_pasando_alcaldia(alcaldia)

   return jsonify({'Status': 'OK', 'Total': len(unidades), 'Records': unidades})