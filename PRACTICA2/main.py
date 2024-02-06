import psycopg2

from create_table import crear_tabla
from create import crear
from delete import eliminar
from update import actualizar
from read import leer
from conn import conexion
from conn import cerrar_conexion



if __name__ == "__main__":
    conn = conexion()

    if conn:
        try:
            #Creación de tabla PELICULAS
            crear_tabla()

            #Insertar valor de la tabla
            pelicula1 = ('1', 'Sherk', '1997', 'x', 'Y', '7.8')
            crear(pelicula1)

            pelicula2 = ('2', 'Sherk 2', '1995', 'x', 'Y', '6.8')
            crear(pelicula2)

            #Eliminar pelicula con id 2
            #eliminar(2)

            #Actualizar valores de la primera tabla
            #pelicula1_update = ('1', 'Sherk', '1995', 'Y', 'X', '7.8', '1')
            #actualizar(pelicula1_update)

            #Leer valores de la tabla
            leer()

        except (Exception, psycopg2.Error) as error:
           print("Error:", error)

        finally:
            cerrar_conexion(conn)