import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Conexión con la base de datos PostgreSQL
conn = psycopg2.connect(
    user = "postgres",
    password = "scared",
    host = "localhost",
    database = "prueba"
)

print("Conexión realizada.")


# Definimos el cursor
cur = conn.cursor()

# Consulta para ejecutar
cur.execute(
    """CREATE TABLE IF NOT EXISTS person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    gender CHAR NOT NULL
    )""")


cur.execute(
    """INSERT INTO person(name, age, gender)
    VALUES ('Frank', 24, 'm'),
    ('Diana', 22, 'f'),
    ('Roberto', 56, 'm'),
    ('Juan', 54, 'm'),
    ('Iker', 45, 'm'),
    ('Pepe', 74, 'm'),
    ('Diego', 62, 'm'),
    ('Roberto', 21, 'm'),
    ('Jacobo', 18, 'm')
    """)

# Enviamos las consultas
conn.commit()
print("Consultas ejecutada.")


# Cerramos el cursor y la conexión.
cur.close()
conn.close()
print("Conexión finalizada.")

# ------------------------------------------------------------------------

# Creación de engine para visualizar base de datos
engine = create_engine('postgresql+psycopg2://postgres:scared@localhost:5432/prueba')

dbconn = engine.connect()

# Utilizamos Pandas para mostrar los datos
#pd.options.display.max_rows <-- configuración para mostrar todos los datos 

df = pd.read_sql_table("person", dbconn, index_col='id')
print(df)