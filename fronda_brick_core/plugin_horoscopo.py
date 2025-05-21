import random

def handle(message):
    signos = ["aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario", "capricornio", "acuario", "piscis"]
    if any(signo in message.lower() for signo in signos) or "horóscopo" in message.lower():
        horoscopos = [
            "Hoy es un buen día para empezar algo nuevo.",
            "Evita discusiones innecesarias, mantén la calma.",
            "La suerte está de tu lado, ¡aprovéchala!",
            "Confía en tu intuición, te guiará correctamente.",
            "Dedica tiempo a tu familia y amigos."
        ]
        return random.choice(horoscopos)
    return None
