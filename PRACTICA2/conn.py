
import psycopg2


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


def cerrar_conexion(conn):
    if conn:
        conn.close()
        print("Connection closed.")

