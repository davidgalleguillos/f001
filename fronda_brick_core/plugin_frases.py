import random

def handle(message):
    frases = [
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "La mejor manera de predecir el futuro es crearlo.",
        "No cuentes los días, haz que los días cuenten.",
        "La creatividad es la inteligencia divirtiéndose.",
        "El único modo de hacer un gran trabajo es amar lo que haces."
    ]
    if "frase" in message.lower() or "motivación" in message.lower():
        return random.choice(frases)
    return None
