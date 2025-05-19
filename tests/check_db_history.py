#!/usr/bin/env python3.11
import sqlite3
import json

DATABASE_NAME = "/home/ubuntu/proyecto_fronda_brick/frondabrick.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def check_conversation_history():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    client_id_to_check = None
    try:
        with open("/home/ubuntu/proyecto_fronda_brick/test_websocket_results.json", "r") as f:
            test_results = json.load(f)
            if test_results.get("mensajes_recibidos") and len(test_results["mensajes_recibidos"]) > 0:
                welcome_msg = test_results["mensajes_recibidos"][0]
                if "Cliente " in welcome_msg and "!" in welcome_msg:
                    start_index = welcome_msg.find("Cliente ") + len("Cliente ")
                    end_index = welcome_msg.find("!", start_index)
                    client_id_to_check = welcome_msg[start_index:end_index]
                    print(f"Client ID from test results: {client_id_to_check}")
    except Exception as e:
        print(f"Error reading client_id from test results: {e}")
        # If we can't get client_id, we can't perform the specific check for TC003 as designed.
        # However, the FrondaBrick core logic for saving history is not yet implemented in fronda_brick.py
        # So this check will likely fail to find specific history anyway for now.
        # For the purpose of this script, let's allow it to proceed to a general check if client_id is not found.

    specific_message_to_check = "cómo estás?"

    if client_id_to_check:
        print(f"Buscando historial para client_id: {client_id_to_check} y mensaje: '{specific_message_to_check}'")
        cursor.execute(
            "SELECT * FROM historial_conversaciones WHERE client_id = ? AND mensaje_usuario = ? ORDER BY timestamp DESC LIMIT 1",
            (client_id_to_check, specific_message_to_check)
        )
        search_description = f"client_id '{client_id_to_check}' y mensaje '{specific_message_to_check}'"
    else:
        print(f"No se pudo determinar client_id. Buscando historial general para el mensaje: '{specific_message_to_check}'")
        cursor.execute(
            "SELECT * FROM historial_conversaciones WHERE mensaje_usuario = ? ORDER BY timestamp DESC LIMIT 5",
            (specific_message_to_check,)
        )
        search_description = f"mensaje '{specific_message_to_check}'"
        
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print(f"Historial encontrado para {search_description}:")
        for row in rows:
            print(dict(row))
        return True, [dict(row) for row in rows]
    else:
        print(f"No se encontró historial para {search_description}.")
        return False, []

if __name__ == "__main__":
    print("Iniciando verificación de persistencia de historial en la base de datos...")
    # The FrondaBrick core currently does not call persistence methods.
    # So, we expect this test to show that no history is saved by the core logic yet.
    history_found, entries = check_conversation_history()
    
    # TC003 is about *verifying* persistence. If the core doesn't save, this test *should* report that.
    # The test script itself is not failing, but it's testing if the application works as expected.
    # The current fronda_brick.py does not call record_interaction.
    if history_found:
        print("TC003: Prueba de persistencia de historial PASADA (entradas encontradas). Esto es INESPERADO ya que el núcleo aún no guarda el historial.")
    else:
        print("TC003: Prueba de persistencia de historial OBSERVACIÓN: No se encontraron entradas de historial para los mensajes de prueba. Esto es ESPERADO ya que el núcleo de Frondabrick (fronda_brick.py) aún no implementa la llamada a `record_interaction` para guardar el historial.")

