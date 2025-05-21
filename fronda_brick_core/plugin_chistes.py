import random

def handle(message):
    chistes = [
        "¿Por qué los programadores confunden Halloween con Navidad? Porque OCT 31 == DEC 25.",
        "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",
        "¿Por qué la computadora fue al médico? Porque tenía un virus.",
        "¿Cómo se despiden los químicos? Ácido un placer.",
        "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas."
    ]
    if "chiste" in message.lower():
        return random.choice(chistes)
    return None
