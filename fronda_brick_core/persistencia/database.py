# fronda_brick_core/persistencia/database.py
import sqlite3
from sqlite3 import Error

DATABASE_NAME = "/home/ubuntu/proyecto_fronda_brick/frondabrick.db"

def create_connection():
    """Crea una conexión a la base de datos SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        print(f"Conexión a SQLite DB establecida: {DATABASE_NAME} (SQLite v{sqlite3.sqlite_version})")
    except Error as e:
        print(f"Error al conectar a SQLite DB: {e}")
    return conn

def create_tables(conn):
    """Crea las tablas necesarias si no existen."""
    sql_create_knowledge_table = """
    CREATE TABLE IF NOT EXISTS conocimiento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        clave TEXT NOT NULL UNIQUE,
        valor TEXT NOT NULL,
        fuente TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """

    sql_create_rules_table = """
    CREATE TABLE IF NOT EXISTS reglas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        regla TEXT NOT NULL UNIQUE,
        descripcion TEXT,
        activa BOOLEAN DEFAULT TRUE,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """

    sql_create_history_table = """
    CREATE TABLE IF NOT EXISTS historial_conversaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id TEXT NOT NULL,
        mensaje_usuario TEXT NOT NULL,
        respuesta_ia TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_knowledge_table)
        cursor.execute(sql_create_rules_table)
        cursor.execute(sql_create_history_table)
        conn.commit()
        print("Tablas creadas o ya existentes.")
    except Error as e:
        print(f"Error al crear tablas: {e}")

# Inicializar la base de datos y las tablas al cargar el módulo
if __name__ == '__main__':
    # Este bloque se ejecuta si se corre el archivo directamente (para setup inicial)
    # En la aplicación, la conexión se manejará de forma más controlada.
    print(f"Intentando inicializar la base de datos en: {DATABASE_NAME}")
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
        conn.close()
        print("Base de datos inicializada y conexión cerrada.")
    else:
        print("No se pudo establecer conexión con la base de datos para la inicialización.")

