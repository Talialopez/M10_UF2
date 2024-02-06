import psycopg2
from conn import conexion

#Se configura recorrer toda la base de datos y leer los valores almacenados
def leer():
    try:
        conn = conexion()
        cursor = conn.cursor()

        sql = ''' SELECT * FROM PELICULAS '''
        cursor.execute(sql)

        #Capta todos los datos por los que recorre el cursor
        resultado = cursor.fetchall()

        #Bucle para que se imprima por terminal los valores que va recorriendo
        for fila in resultado:
            print(fila)

        return resultado
    except  (Exception, psycopg2.Error) as error:
        print("Error para leer valores:", error)