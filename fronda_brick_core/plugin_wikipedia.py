import requests

def handle(message):
    if message.lower().startswith("wiki "):
        termino = message[5:].strip().replace(' ', '_')
        try:
            r = requests.get(f"https://es.wikipedia.org/api/rest_v1/page/summary/{termino}", timeout=3)
            if r.status_code == 200:
                data = r.json()
                if 'extract' in data:
                    return f"Wikipedia: {data['extract']}"
        except Exception:
            pass
        return f"No encontré información en Wikipedia sobre {termino}."
    return None
