from . import config as cnf

import sqlite3


def connect():
    con = sqlite3.connect(cnf.path_bd)

    return con


def query_insert_registros(tabla: str, registros: list, columnas: tuple = ()):
    """
    :param tabla: nombre de la tabla
    :param columnas:
    :param registros:
    :return: 'INSERT INTO tabla (columna1, columna2,...) VALUES (registro1, registro2, ...), (r2, r,...)'
    """
    query_columnas = "(`" + "`, `".join(columnas) + "`)" if columnas else ''

    temporal = []

    for registro in registros:
        if not registro:
            continue

        registro_empaquetado = empaquetamiento_de_registro(registro)

        temporal.append(registro_empaquetado)

    query_values = ", ".join(temporal)

    return '''
        INSERT INTO 
            {tabla} {columnas} 
        VALUES
            {values}
    '''.format(tabla=tabla, columnas=query_columnas, values=query_values)


def empaquetamiento_de_registro(registro: list):
    regtemp = [x if x is not None else 'NoneReserveRemplace' for x in registro]

    empaquetado = str(tuple(regtemp)) if len(regtemp) > 1 else str(tuple(regtemp))[:-2] + ')'

    return empaquetado.replace("\'NoneReserveRemplace\'", 'null')


class BD:
    def __init__(self):
        self.con = connect()

    def __del__(self):
        self.con.close()

    def abrircursor(self):
        return self.con.cursor()

    def execute(self, sql):
        cursor = self.abrircursor()

        try:
            cursor.execute(sql)
            self.con.commit()
        except sqlite3.Error as e:
            self.con.rollback()
            self.cerrar_cursor(cursor)

            raise e

        self.cerrar_cursor(cursor)

    def select(self, sql, data=()):
        cursor = self.abrircursor()

        try:
            cursor.execute(sql) if not data else cursor.execute(sql, data)
            resp = cursor.fetchall()
            self.cerrar_cursor(cursor)

            return resp
        except sqlite3.Error as e:
            self.cerrar_cursor(cursor)
            raise e

    @staticmethod
    def cerrar_cursor(cursor):
        cursor.close()
