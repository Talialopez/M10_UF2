
import psycopg2

#Iniciaciando conexión mediante valores que se ingresaron en pgadmin
def conexion():
    try:
        conn = psycopg2.connect(
            database="postgres",
            user='user_postgres',
            password='pass_postgres',
            host='localhost',
            port='5432',
        )
        
        return conn
    
    except  (Exception, psycopg2.Error) as error:
        print("Error para conectar:", error)

#Cerrando conexión
def cerrar_conexion(conn):
    if conn:
        conn.close()
        print("Conexion cerrada.")

