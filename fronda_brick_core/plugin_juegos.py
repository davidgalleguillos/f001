import random

def handle(message):
    if "adivina" in message.lower():
        num = random.randint(1,10)
        return f"Adivina un número del 1 al 10... (Pista: es {num})"
    if "piedra papel o tijera" in message.lower():
        jugada = random.choice(["piedra", "papel", "tijera"])
        return f"Yo elijo: {jugada}"
    return None
