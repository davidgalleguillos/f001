import requests

def handle(message):
    if message.lower().startswith("define ") or message.lower().startswith("definicion de "):
        palabra = message.split(" ", 1)[1].strip()
        try:
            resp = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/es/{palabra}", timeout=3)
            if resp.status_code == 200:
                data = resp.json()
                definicion = data[0]['meanings'][0]['definitions'][0]['definition']
                return f"Definición de {palabra}: {definicion}"
        except Exception:
            pass
        return f"No encontré la definición de {palabra}."
    return None
