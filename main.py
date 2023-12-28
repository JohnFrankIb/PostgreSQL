import psycopg2
import pandas as pd


# Conexión con la base de datos PostgreSQL
conn = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "scared",
    database = "prueba"
)

print("Conexión exitosa.")

# Definimos el cursor
cur = conn.cursor()

# Consulta para ejecutar
cur.execute("""CREATE TABLE IF NOT EXISTS person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    age INT,
    gender CHAR
    )""")


cur.execute("""INSERT INTO person (name, age, gender) VALUES
            (1, "Mike", 30, "m"),
            (2, "Lisa", 30, "f"),
            (3, "John", 54, "m"),
            (4, "Bob", 80, "m"),
            (5, "Julie", 40, "f")
            """)

# Enviamos las consultas
conn.commit()
print("Consultas ejecutada.")


# Cerramos el cursor y la conexión.
cur.close()
conn.close()
print("Conexión finalizada.")