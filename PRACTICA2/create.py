import psycopg2
from conn import conexion

#Insertamos valores a una tabla gracias a la consulta sql, en caso de error, salta el error programado más adelante
def crear(valores):
    try:
        conn = conexion()
        cursor = conn.cursor()
    
        sql = ''' INSERT INTO PELICULAS (ID, TITULO, ANIO, DIRECTOR, GENERO, PUNTUACION) 
                        VALUES (%s, %s, %s, %s, %s, %s)'''
        
        cursor.execute(sql, (valores))
        conn.commit()

    except  (Exception, psycopg2.Error) as error:
        print("Error para insertar valores:", error)