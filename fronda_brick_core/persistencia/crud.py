# fronda_brick_core/persistencia/crud.py
import sqlite3
from .database import DATABASE_NAME #, create_connection # Assuming create_connection is used per operation or managed outside

def get_db_connection():
    """Helper function to get a new database connection."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row # Access columns by name
    return conn

# --- Operaciones para Conocimiento ---
def add_knowledge(clave: str, valor: str, fuente: str = None) -> int:
    """Añade un nuevo hecho a la base de conocimiento."""
    conn = get_db_connection()
    sql = "INSERT INTO conocimiento (clave, valor, fuente) VALUES (?, ?, ?)"
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (clave, valor, fuente))
        conn.commit()
        print(f"Conocimiento añadido: {clave} -> {valor}")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Error: La clave de conocimiento 
{clave}
 ya existe.")
        return None
    finally:
        conn.close()

def get_knowledge(clave: str):
    """Recupera un hecho de la base de conocimiento por su clave."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM conocimiento WHERE clave = ?", (clave,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def update_knowledge(clave: str, nuevo_valor: str, nueva_fuente: str = None):
    """Actualiza un hecho existente en la base de conocimiento."""
    conn = get_db_connection()
    sql = "UPDATE conocimiento SET valor = ?, fuente = ?, timestamp = CURRENT_TIMESTAMP WHERE clave = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (nuevo_valor, nueva_fuente, clave))
    conn.commit()
    updated_rows = cursor.rowcount
    conn.close()
    if updated_rows > 0:
        print(f"Conocimiento actualizado para la clave: {clave}")
    else:
        print(f"No se encontró conocimiento para actualizar con la clave: {clave}")
    return updated_rows > 0

def delete_knowledge(clave: str):
    """Elimina un hecho de la base de conocimiento."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM conocimiento WHERE clave = ?", (clave,))
    conn.commit()
    deleted_rows = cursor.rowcount
    conn.close()
    if deleted_rows > 0:
        print(f"Conocimiento eliminado para la clave: {clave}")
    else:
        print(f"No se encontró conocimiento para eliminar con la clave: {clave}")
    return deleted_rows > 0

# --- Operaciones para Reglas ---
def add_rule(regla: str, descripcion: str = None, activa: bool = True) -> int:
    """Añade una nueva regla."""
    conn = get_db_connection()
    sql = "INSERT INTO reglas (regla, descripcion, activa) VALUES (?, ?, ?)"
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (regla, descripcion, activa))
        conn.commit()
        print(f"Regla añadida: {regla}")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Error: La regla 
{regla}
 ya existe.")
        return None
    finally:
        conn.close()

def get_rule(regla_str: str):
    """Recupera una regla por su contenido."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reglas WHERE regla = ?", (regla_str,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

# --- Operaciones para Historial de Conversaciones ---
def add_conversation_history(client_id: str, mensaje_usuario: str, respuesta_ia: str) -> int:
    """Añade una interacción al historial de conversaciones."""
    conn = get_db_connection()
    sql = "INSERT INTO historial_conversaciones (client_id, mensaje_usuario, respuesta_ia) VALUES (?, ?, ?)"
    cursor = conn.cursor()
    cursor.execute(sql, (client_id, mensaje_usuario, respuesta_ia))
    conn.commit()
    history_id = cursor.lastrowid
    conn.close()
    print(f"Historial de conversación añadido para {client_id}, ID: {history_id}")
    return history_id

def get_conversation_history(client_id: str, limit: int = 10):
    """Recupera el historial de conversaciones para un cliente específico."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM historial_conversaciones WHERE client_id = ? ORDER BY timestamp DESC LIMIT ?",
        (client_id, limit)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# Ejemplo de uso (para pruebas directas del módulo)
if __name__ == '__main__':
    # Asegúrate de que database.py ha sido ejecutado al menos una vez para crear el .db y las tablas
    print("Probando operaciones CRUD...")
    # Conocimiento
    add_knowledge("color_cielo", "azul", "observacion_comun")
    knowledge = get_knowledge("color_cielo")
    print(f"Conocimiento recuperado: {knowledge}")
    update_knowledge("color_cielo", "azul claro", "observacion_matutina")
    knowledge = get_knowledge("color_cielo")
    print(f"Conocimiento actualizado: {knowledge}")
    # delete_knowledge("color_cielo")

    # Reglas
    add_rule("SI pregunta_saludo RESPONDER saludo_cordial", "Responde a saludos de forma amigable")
    rule = get_rule("SI pregunta_saludo RESPONDER saludo_cordial")
    print(f"Regla recuperada: {rule}")

    # Historial
    add_conversation_history("test_client_crud", "Hola Fronda", "Hola! Soy Frondabrick.")
    history = get_conversation_history("test_client_crud")
    print(f"Historial recuperado: {history}")

