from create_table import crear_tabla
from create import crear
from delete import eliminar
from update import actualizar
from read import leer



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

        #Eliminar valor de una tabla
        #eliminar(pelicula2)

        #Actualizar valores de la primera tabla
        #pelicula1_update = ('1', 'Sherk', '1995', 'Y', 'X', '7.8')

        #Leer valores de la tabla
        #leer()

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        cerrar_conexion(conn)