from conn import conexion

#Se configura eliminar pelicula segun ID
def eliminar(valores):
    try:
        conn = conexion()
        cursor = conn.cursor()

        sql = '''DELETE FROM PELICULAS WHERE id = %s'''
        cursor.execute(sql, (valores))

        conn.commit()

    except  (Exception, psycopg2.Error) as error:
        print("Error para eliminar valores:", error)