from conn import conexion

def crear(valores):
    conn = conexion()
    cursor = conn.cursor()

    sql = ''' INSERT INTO PELICULAS (ID, TITULO, ANIO, DIRECTOR, GENERO, PUNTUACION) 
                    VALUES (%s, %s, %s, %s, %s, %s)'''
    
    cursor.execute(sql, valores)
    conn.commit()