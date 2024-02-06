import psycopg2
from conn import conexion

#Se configura actualizar valores
def actualizar(valores):
    try:
        conn = conexion()
        cursor = conn.cursor()

        sql = '''UPDATE PELICULAS 
                SET TITULO = %s, ANIO = %s, DIRECTOR = %s, GENERO = %s, PUNTUACION = %s WHERE id = %s'''

        cursor.execute(sql, valores)
        conn.commit()
        
    except  (Exception, psycopg2.Error) as error:
        print("Error para actualizar valores: ", error)
