import requests

def handle(message):
    if message.lower().startswith("traduce "):
        texto = message[8:]
        try:
            resp = requests.get(f"https://api.mymemory.translated.net/get?q={texto}&langpair=es|en", timeout=3)
            if resp.status_code == 200:
                data = resp.json()
                traduccion = data['responseData']['translatedText']
                return f"Traducción al inglés: {traduccion}"
        except Exception:
            pass
        return "No pude traducir el texto."
    return None
