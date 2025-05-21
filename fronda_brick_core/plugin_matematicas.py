import re

def handle(message):
    # Resuelve operaciones matemáticas simples
    match = re.match(r"(\d+)\s*([+\-*/])\s*(\d+)", message.replace(',', '.'))
    if match:
        a, op, b = match.groups()
        a, b = float(a), float(b)
        if op == '+': return str(a + b)
        if op == '-': return str(a - b)
        if op == '*': return str(a * b)
        if op == '/':
            if b == 0:
                return "No se puede dividir por cero."
            return str(a / b)
    return None
