
import psycopg2


# Conexión con la base de datos PostgreSQL
try:
    conn = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "scared",
        database = "prueba"
    )

    print("Conexión exitosa.")

except Exception as ex:
    print(ex)
finally:
    conn.close()
    print("Conexión finalizada.")