from conn import conexion

def leer():
    conn = conexion()
    cursor = conn.cursor()

    sql = ''' SELECT * FROM PELICULAS '''
    cursor.execute(sql)
    resultado = cursor.fetchall()

    return resultado