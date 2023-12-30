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


# Definimos el cursor
cur = conn.cursor()

# Consultas para ejecutar

def new_table():
    cur.execute(
        """CREATE TABLE IF NOT EXISTS person (
        id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        age INT NOT NULL,
        gender CHAR NOT NULL
        )""")
    conn.commit()
    print("Tabla creada.")
    cur.close()
    conn.close
    print("Conexión finalizada.")

def query():
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
    conn.commit()
    print("Consulta ejecutada")
    cur.close()
    conn.close()
    print("Conexión finalizada.")

def new_query():
    cur.execute(
        """SELECT DISTINCT name
        FROM person;
        """)
    cur.close()
    conn.close()
    print("Conexión finalizada.")

query = """SELECT DISTINCT name
    FROM person;
    """
cur.close()
conn.close()

# ------------------------------------------------------------------------

#   Creación de engine para visualizar base de datos con SQLAlchemy
engine = create_engine('postgresql+psycopg2://postgres:scared@localhost:5432/prueba')
enconn = engine.connect()

#   Utilizamos Pandas para mostrar los datos
#pd.options.display.max_rows <-- configuración para mostrar todos los datos 

df = pd.read_sql_query(query, enconn)
print(df)

enconn.close


# ARREGLAR LAS FUNCIONES (SQLALCHEMY NO PUEDE TRABAJAR CON FUNCIONES)
# ASIGNAR LAS FUNCIONES A VARIABLES