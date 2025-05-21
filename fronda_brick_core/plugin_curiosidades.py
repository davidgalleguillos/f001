import random

def handle(message):
    curiosidades = [
        "Las abejas pueden reconocer rostros humanos.",
        "El corazón de un camarón está en su cabeza.",
        "Los delfines duermen con un ojo abierto.",
        "La miel nunca se echa a perder.",
        "Los pulpos tienen tres corazones."
    ]
    if "curiosidad" in message.lower() or "dato curioso" in message.lower():
        return random.choice(curiosidades)
    return None
