import spacy
from typing import Optional, Dict, Any

class PluginNlp:
    def __init__(self):
        self.nlp = None
        self.load_model()
    
    def load_model(self):
        """Carga el modelo de spaCy en español."""
        try:
            self.nlp = spacy.load("es_core_news_sm")
            print("✅ Plugin NLP: Modelo de lenguaje cargado correctamente.")
        except OSError:
            print("❌ Error: No se encontró el modelo de spaCy. Ejecuta en Google Colab:")
            print("!python -m spacy download es_core_news_sm")
            self.nlp = None
    
    def handle(self, message: str, context: Optional[Dict[str, Any]] = None) -> Optional[str]:
        """Método principal que maneja los mensajes entrantes."""
        if not self.nlp:
            return None
        
        doc = self.nlp(message.lower())
        
        # Ejemplo: Si el mensaje es un saludo
        if any(token.text in message.lower() for token in doc if token.is_alpha):
            if any(token.lemma_ in ["hola", "saludos", "buenos", "buenas"] for token in doc):
                return "¡Hola! Soy Frondabrick, ¿en qué puedo ayudarte hoy?"
        
        # Ejemplo: Si el mensaje pregunta por el clima
        if any(token.lemma_ in ["clima", "tiempo"] for token in doc):
            return "No tengo acceso al clima actual, pero puedo ayudarte con otras cosas. 😊"
        
        # Ejemplo: Si el mensaje menciona programación
        if any(token.lemma_ in ["programar", "python", "código"] for token in doc):
            return "¡Me encanta programar! ¿Necesitas ayuda con algún código en Python?"
        
        # Si no se reconoce el mensaje, devuelve None para que otro plugin lo maneje
        return None

# Instancia del manejador para ser importada por el sistema de plugins
handle = PluginNlp().handle
