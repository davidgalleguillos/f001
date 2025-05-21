import requests

def handle(message):
    if "noticia" in message.lower():
        try:
            r = requests.get("https://newsapi.org/v2/top-headlines?country=mx&apiKey=demo", timeout=3)
            if r.status_code == 200:
                data = r.json()
                if data['articles']:
                    art = data['articles'][0]
                    return f"Noticia: {art['title']}\n{art['url']}"
        except Exception:
            pass
        return "No pude obtener noticias en este momento."
    return None
