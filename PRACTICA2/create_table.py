from conn import conexion


def crear_tabla():
    conn = conexion()
    cursor = conn.cursor()

    sql = '''CREATE TABLE PELICULAS(
                    ID SERIAL PRIMARY KEY,
                    TITULO VARCHAR(255) NOT NULL,
                    ANIO VARCHAR(255) NOT NULL,
                    DIRECTOR VARCHAR(255) NOT NULL,
                    GENERO VARCHAR(255) NOT NULL,
                    PUNTUACION FLOAT NOT NULL

    )'''

    cursor.execute(sql)
    conn.commit()