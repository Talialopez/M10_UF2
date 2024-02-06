# update.py
from conn import conexion

def actualizar():
    conn = conexion()
    cursor = conn.cursor()

    sql = '''UPDATE PELICULAS 
             SET ID = %s, TITULO = %s, ANIO = %s, DIRECTOR = %s, GENERO = %s, PUNTUACION = %s
             WHERE id = %s'''

    conn.commit()

