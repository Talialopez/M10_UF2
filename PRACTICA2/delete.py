from conn import conexion

def eliminar(valor):
    conn = conexion()
    cursor = conn.cursor()

    sql = '''DELETE FROM PELICULAS WHERE id = %s'''
    cursor.execute(sql, (valor,))

    conn.commit()

