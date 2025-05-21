import re
import math

def handle(message):
    # Calculadora científica básica
    try:
        if message.lower().startswith("calcula "):
            expr = message[8:].replace('^', '**')
            # Solo permitir caracteres seguros
            if not re.match(r'^[\d\s\+\-\*/\(\)\.eE,\^]+$', expr):
                return "Expresión no permitida."
            resultado = eval(expr, {"__builtins__": None, "math": math}, {})
            return f"Resultado: {resultado}"
    except Exception:
        return "No pude calcular esa expresión."
    return None
