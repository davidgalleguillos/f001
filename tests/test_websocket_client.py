#!/usr/bin/env python3.11
import asyncio
import websockets
import json

async def test_frondabrick_websocket():
    uri = "ws://localhost:8000/ws/chat"
    results = {
        "TC001_conexion_exitosa": False,
        "TC002_envio_recepcion_hola": False,
        "TC003_persistencia_historial": False, # Placeholder, will be checked via DB
        "TC004_intento_aprendizaje": False, # Placeholder, will be checked via logs/DB
        "mensajes_recibidos": []
    }
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Conectado a {uri}")
            results["TC001_conexion_exitosa"] = True
            
            # Esperar mensaje de bienvenida
            welcome_message = await websocket.recv()
            print(f"< {welcome_message}")
            results["mensajes_recibidos"].append(welcome_message)
            if "Bienvenido" in welcome_message and "Frondabrick" in welcome_message:
                print("TC001: Mensaje de bienvenida recibido.")

            # TC002: Enviar "hola" y verificar respuesta
            test_message_hola = "hola"
            print(f"> {test_message_hola}")
            await websocket.send(test_message_hola)
            
            # Recibir dos mensajes: el eco y la respuesta del core
            response_echo_hola = await websocket.recv() # El router actual envia un eco primero
            print(f"< {response_echo_hola}")
            results["mensajes_recibidos"].append(response_echo_hola)

            response_core_hola = await websocket.recv() # Luego la respuesta del core
            print(f"< {response_core_hola}")
            results["mensajes_recibidos"].append(response_core_hola)
            if "Hola! Soy Frondabrick" in response_core_hola:
                results["TC002_envio_recepcion_hola"] = True
                print("TC002: Respuesta a 'hola' recibida correctamente.")
            else:
                print(f"TC002: Respuesta inesperada a 'hola': {response_core_hola}")

            # TC004: Simular intento de aprendizaje (flujo)
            test_message_aprender = "aprender que los pájaros vuelan"
            print(f"> {test_message_aprender}")
            await websocket.send(test_message_aprender)
            response_echo_aprender = await websocket.recv()
            print(f"< {response_echo_aprender}")
            results["mensajes_recibidos"].append(response_echo_aprender)
            response_core_aprender = await websocket.recv()
            print(f"< {response_core_aprender}")
            results["mensajes_recibidos"].append(response_core_aprender)
            if "He registrado tu solicitud de aprendizaje" in response_core_aprender:
                 # Esto es un placeholder, la prueba real implicaría verificar logs o DB
                results["TC004_intento_aprendizaje"] = True
                print("TC004: Respuesta a intento de 'aprender' recibida.")
            else:
                print(f"TC004: Respuesta inesperada a 'aprender': {response_core_aprender}")

            # Enviar un mensaje para probar el historial
            test_message_historial = "cómo estás?"
            print(f"> {test_message_historial}")
            await websocket.send(test_message_historial)
            response_echo_historial = await websocket.recv()
            print(f"< {response_echo_historial}")
            results["mensajes_recibidos"].append(response_echo_historial)
            response_core_historial = await websocket.recv()
            print(f"< {response_core_historial}")
            results["mensajes_recibidos"].append(response_core_historial)
            # La verificación de TC003 se hará revisando la base de datos después.

    except Exception as e:
        print(f"Error durante la prueba WebSocket: {e}")
    finally:
        print("\nResultados de la prueba:")
        print(json.dumps(results, indent=4))
        with open("/home/ubuntu/proyecto_fronda_brick/test_websocket_results.json", "w") as f:
            json.dump(results, f, indent=4)
        print("\nResultados guardados en /home/ubuntu/proyecto_fronda_brick/test_websocket_results.json")

if __name__ == "__main__":
    asyncio.run(test_frondabrick_websocket())

