import psycopg2
from conn import conexion

#Creamos tabla en caso de que no exista.
def crear_tabla():
    try:
        conn = conexion()
        cursor = conn.cursor()

        #Consulta sql que se ejecutara gracias al cursor que recorrera la base de datos.
        sql = '''CREATE TABLE IF NOT EXISTS PELICULAS(
                        ID SERIAL PRIMARY KEY,
                        TITULO VARCHAR(255) NOT NULL,
                        ANIO VARCHAR(255) NOT NULL,
                        DIRECTOR VARCHAR(255) NOT NULL,
                        GENERO VARCHAR(255) NOT NULL,
                        PUNTUACION FLOAT NOT NULL

        )'''

        #Ejecución de la consulta.
        cursor.execute(sql)
        #Se guarda la ejecución hecha anteriormente.
        conn.commit()

    except  (Exception, psycopg2.Error) as error:
        print("Error creación tabla:", error)