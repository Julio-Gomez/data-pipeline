from app import app


@app.route('unidades/<disponibles>', methods=('GET',))
def unidades_disponibles(disponibles):
   pass


@app.route('ubicaciones/fechas/<id>', methods=('GET',))
def historial_ubicfec(id):
   pass


@app.route('alcaldias/<disponibles>', methods=('GET',))
def alcaldias_disponibles(id):
   pass


@app.route('alcaldias/<alcadia>', methods=('GET',))
def unidades_pasando_alcadia(alcaldia):
   pass