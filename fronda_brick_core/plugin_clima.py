import requests

def handle(message):
    if "clima" in message.lower():
        ciudad = None
        palabras = message.lower().split()
        if "en" in palabras:
            idx = palabras.index("en")
            if idx+1 < len(palabras):
                ciudad = palabras[idx+1]
        if not ciudad:
            ciudad = "Santiago"
        try:
            r = requests.get(f"https://wttr.in/{ciudad}?format=3", timeout=3)
            if r.status_code == 200:
                return r.text
        except Exception:
            pass
        return f"No pude obtener el clima para {ciudad}."
    return None
