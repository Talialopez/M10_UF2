from conn import conexion

#Se configura recorrer toda la base de datos y leer los valores almacenados
def leer():
    try:
        conn = conexion()
        cursor = conn.cursor()

        sql = ''' SELECT * FROM PELICULAS '''
        cursor.execute(sql)
        resultado = cursor.fetchall()

        return resultado
    except  (Exception, psycopg2.Error) as error:
        print("Error para leer valores:", error)