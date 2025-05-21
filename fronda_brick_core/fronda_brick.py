# fronda_brick_core/fronda_brick.py

# Import persistence and learning modules when they are defined
# from .persistencia import crud as persistence_module
# from .modulos import aprendizaje

import importlib.util
import os
import glob

class FrondaBrick:
    def log_experience(self, client_id, message):
        """
        Registra la experiencia/interacción recibida de un cliente (puede ser extendido para persistencia).
        """
        print(f"[LOG EXPERIENCE] Cliente: {client_id}, Mensaje: {message}")

    def save_experience(self, client_id, message, response):
        """
        Guarda la experiencia de interacción en la base de datos y activa aprendizaje avanzado.
        """
        try:
            # Guardar en la base de datos
            from fronda_brick_core.persistencia import crud
            crud.add_conversation_history(client_id, message, response)
            print(f"[SAVE EXPERIENCE] Guardado en DB para Cliente: {client_id}")
        except Exception as e:
            print(f"[SAVE EXPERIENCE] Error al guardar en DB: {e}")

        # Activar heurística avanzada o aprendizaje adicional
        # 1. Aprendizaje supervisado inmediato
        self.learn(message, response)
        print("[SAVE EXPERIENCE] Aprendizaje supervisado activado.")

        # 2. (Opcional) Entrenamiento adicional, reglas, etc.
        # self.train(epochs=1)  # Descomentar si quieres entrenamiento incremental
        # Aquí puedes activar otras heurísticas, módulos o librerías avanzadas
    def __init__(self):
        """
        Inicializa el núcleo de Frondabrick con una red neuronal simple y memoria de entrenamiento.
        """
        from collections import deque
        self.memory = deque(maxlen=1000)  # Memoria de interacciones (input, output) limitada a 1000 elementos
        self.vocab = {}   # Diccionario para vectorizar palabras
        self.output_vocab = {} # Diccionario para respuestas
        self.input_size = 20  # Longitud máxima de entrada (palabras)
        self.hidden_size = 16 # Tamaño de la capa oculta
        self.output_size = 20 # Longitud máxima de salida (palabras)
        # Pesos de la red (simple perceptrón multicapa)
        import numpy as np
        self.W1 = np.random.randn(self.input_size, self.hidden_size) * 0.1
        self.b1 = np.zeros((self.hidden_size,))
        self.W2 = np.random.randn(self.hidden_size, self.output_size) * 0.1
        self.b2 = np.zeros((self.output_size,))
        print("Núcleo de Frondabrick inicializado con red neuronal simple.")

        # --- Cargar plugins dinámicamente ---
        self.plugins = []
        plugins_dir = os.path.dirname(os.path.abspath(__file__))
        for plugin_path in glob.glob(os.path.join(plugins_dir, "plugin_*.py")):
            plugin_name = os.path.splitext(os.path.basename(plugin_path))[0]
            if plugin_name == "__init__":
                continue
            try:
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, "handle"):
                    self.plugins.append(module.handle)
                    print(f"Plugin cargado: {plugin_name}")
            except Exception as e:
                print(f"Error al cargar el plugin {plugin_name}: {e}")

        # Aprendizaje manual: enseñar ejemplos útiles a Fronda
        self.learn("hola", "¡Hola! ¿En qué puedo ayudarte?")
        self.learn("¿quién eres?", "Soy Frondabrick, una IA modular y avanzada.")
        self.learn("¿quién te creó?", "Me creó David Galleguillos Ruiz, alias Fronda Brick.")
        self.learn("¿cuál es la capital de Francia?", "La capital de Francia es París.")
        self.learn("¿qué es una red neuronal?", "Una red neuronal es un modelo computacional inspirado en el cerebro humano.")
        self.learn("adiós", "¡Hasta luego! Fue un gusto conversar contigo.")
        self.learn("¿cómo estás?", "Estoy funcionando correctamente y lista para ayudarte.")
        self.learn("¿qué puedes hacer?", "Puedo conversar, aprender y ayudarte con información útil.")
        self.learn("¿cuál es tu versión?", "Mi versión es 0.01.")
        self.learn("¿qué es la niebla?", "La niebla es un entorno de computación distribuida localmente.")
        # Entrenamiento inicial con los ejemplos dados
        # self.train(epochs=20)  # Entrenamiento inicial solo si es necesario, desactivado para evitar consumo excesivo

    def process_message(self, client_id: str, message: str) -> str:
        """
        Razonador central: elige el mejor módulo según el conocimiento y capacidades disponibles.
        Siempre usa el módulo más avanzado posible. Además, aprende de cada interacción y se auto-mejora.
        """
        self.log_experience(client_id, message)

        # --- Despacho a plugins ---
        for plugin_handle in getattr(self, "plugins", []):
            try:
                plugin_response = plugin_handle(message)
                if plugin_response is not None:
                    response = plugin_response
                    break
            except Exception as e:
                print(f"Error en plugin: {e}")
        else:
            heuristica = self.heuristic_response(message)
            if heuristica is not None:
                response = heuristica
            else:
                llm_response = self.transformer_module(message)
                if not llm_response.startswith("[LLM real no configurado"):
                    response = llm_response
                else:
                    response = "Actualmente no tengo un módulo adecuado para esta tarea. Estoy en constante mejora y pronto podré responder a todo tipo de preguntas."
        self.memory.append((message, response))
        self.save_experience(client_id, message, response)
        # self.auto_improve()  # Desactivado para evitar consumo excesivo en cada mensaje
        print(f"Núcleo responde a {client_id}: {response}")
        return response

    def heuristic_response(self, message: str) -> str:
        """
        Heurística avanzada y ligera: patrones, reglas, sinónimos, generalización y similitud eficiente.
        Carga saludos, despedidas y reglas desde archivos externos para expansión infinita.
        """
        import re, math, ast, difflib, os, json
        msg = message.strip().lower()
        base_path = os.path.join(os.path.dirname(__file__), "data")

        # 1. Responder a saludos y despedidas con sinónimos externos
        def cargar_lista(nombre):
            try:
                with open(os.path.join(base_path, f"{nombre}.txt"), encoding="utf-8") as f:
                    return [line.strip().lower() for line in f if line.strip()]
            except Exception:
                # Fallback si no existe el archivo
                if nombre == "saludos":
                    return ["hola", "buenas", "saludos", "holi", "holaa", "buenos días", "buenas tardes", "buenas noches"]
                if nombre == "despedidas":
                    return ["adiós", "chao", "hasta luego", "nos vemos", "bye", "me despido"]
                return []
        saludos = cargar_lista("saludos")
        despedidas = cargar_lista("despedidas")
        if any(s in msg for s in saludos):
            return "¡Hola! ¿En qué puedo ayudarte?"
        if any(d in msg for d in despedidas):
            return "¡Hasta luego! Fue un gusto conversar contigo."

        # 2. Generalización: ¿quién es ...?
        match = re.match(r"¿quién es ([\w\sáéíóúüñ\-\.]+)\??", msg)
        if match:
            persona = match.group(1).strip().capitalize()
            return f"No tengo información detallada sobre {persona}, pero puedo ayudarte a buscar en Wikipedia: https://es.wikipedia.org/wiki/{persona.replace(' ', '_')}"

        # 3. Generalización: ¿cuál es la capital de ...?
        match = re.match(r"¿cu[aá]l es la capital de ([\w\sáéíóúüñ\-\.]+)\??", msg)
        if match:
            pais = match.group(1).strip().capitalize()
            return f"No tengo una base de datos completa de países, pero puedes consultar rápidamente aquí: https://es.wikipedia.org/wiki/Anexo:Capitales_de_Europa o buscar '{pais} capital' en Google."

        # 4. Reglas básicas IF-THEN desde archivo externo
        reglas = {}
        try:
            with open(os.path.join(base_path, "reglas.json"), encoding="utf-8") as f:
                reglas = json.load(f)
        except Exception:
            reglas = {
                "el sol es una estrella": "Correcto, el Sol es una estrella ubicada en el centro del sistema solar.",
                "la tierra es un planeta": "Así es, la Tierra es el tercer planeta del sistema solar."
            }
        for clave, valor in reglas.items():
            if clave in msg:
                return valor

        # 5. Matemáticas avanzadas
        if any(word in msg for word in ["integral", "derivada", "límite", "matriz", "ecuación diferencial"]):
            return self.math_module(message)
        # 6. Procesamiento de lenguaje natural avanzado (transformer)
        if any(word in msg for word in ["conversa", "charla", "explica", "resume", "traduce"]):
            return self.transformer_module(message)
        # 7. Visión artificial / cámara / análisis de imágenes
        if any(word in msg for word in ["mira", "imagen", "foto", "cámara", "dibujo", "analiza imagen"]):
            return self.vision_module(message)
        # 8. Otros módulos futuros
        if "audio" in msg:
            return self.audio_module(message)
        if "robot" in msg:
            return self.robotics_module(message)

        # 9. Coincidencia exacta o cercana con frases aprendidas
        for input_text, output_text in reversed(self.memory):
            if msg == input_text.strip().lower():
                return output_text
        entradas = [input_text for input_text, _ in self.memory]
        matches = difflib.get_close_matches(msg, entradas, n=1, cutoff=0.8)
        if matches:
            for input_text, output_text in reversed(self.memory):
                if input_text.strip().lower() == matches[0]:
                    return output_text
        # 10. Si no hay coincidencia, None
        return None

    def learn(self, input_text: str, output_text: str):
        """
        Aprende una nueva asociación entre entrada y salida usando un paso de entrenamiento supervisado (tipo perceptrón).
        """
        import numpy as np
        x = self.vectorize_input(input_text)
        y_true = self.vectorize_output(output_text)
        # Forward
        z1 = np.dot(x, self.W1) + self.b1
        a1 = np.tanh(z1)
        z2 = np.dot(a1, self.W2) + self.b2
        # Softmax para salida
        exp_scores = np.exp(z2 - np.max(z2))
        y_pred = exp_scores / np.sum(exp_scores)
        # Backpropagation (descenso de gradiente simple)
        lr = 0.01
        dz2 = y_pred - y_true
        dW2 = np.outer(a1, dz2)
        db2 = dz2
        da1 = np.dot(self.W2, dz2)
        dz1 = da1 * (1 - np.tanh(z1)**2)
        dW1 = np.outer(x, dz1)
        db1 = dz1
        # 1. Ecuaciones universales y explicaciones de grandes mentes
        # --- Cálculo activo para ecuaciones famosas ---
        import re
        # E=mc^2
        match_emc2 = re.search(r'calcula(r)?\s*e\s*=\s*m\s*c\^?2.*m\s*=\s*([\d\.eE\+\-]+).*c\s*=\s*([\d\.eE\+\-]+)', message.lower().replace(',', '.'))
        if match_emc2:
            try:
                m = float(match_emc2.group(2))
                c = float(match_emc2.group(3))
                E = m * c ** 2
                return f"E = m·c² = {m} * {c}² = {E}"
            except Exception as e:
                return f"No pude calcular E=mc²: {e}"
        # F=ma
        match_fma = re.search(r'calcula(r)?\s*f\s*=\s*m\s*a.*m\s*=\s*([\d\.eE\+\-]+).*a\s*=\s*([\d\.eE\+\-]+)', message.lower().replace(',', '.'))
        if match_fma:
            try:
                m = float(match_fma.group(2))
                a = float(match_fma.group(3))
                F = m * a
                return f"F = m·a = {m} * {a} = {F}"
            except Exception as e:
                return f"No pude calcular F=ma: {e}"
        # Teorema de Pitágoras a^2 + b^2 = c^2
        match_pitagoras = re.search(r'calcula(r)?\s*c\s*=\s*raiz\s*\(?a\^?2\s*\+\s*b\^?2\)?\s*a\s*=\s*([\d\.eE\+\-]+).*b\s*=\s*([\d\.eE\+\-]+)', message.lower().replace(',', '.'))
        if match_pitagoras:
            try:
                a = float(match_pitagoras.group(2))
                b = float(match_pitagoras.group(3))
                import math
                c = math.sqrt(a**2 + b**2)
                return f"c = sqrt(a² + b²) = sqrt({a}² + {b}²) = {c}"
            except Exception as e:
                return f"No pude calcular el teorema de Pitágoras: {e}"
        # --- Explicaciones si solo se menciona la ecuación ---
        ecuaciones_famosas = {
            "e=mc^2": "La ecuación de Einstein para la equivalencia masa-energía: E = m·c², donde E es energía, m es masa y c es la velocidad de la luz.",
            "f=ma": "La segunda ley de Newton: F = m·a, fuerza es igual a masa por aceleración.",
            "a^2+b^2=c^2": "El teorema de Pitágoras: en un triángulo rectángulo, la suma de los cuadrados de los catetos es igual al cuadrado de la hipotenusa.",
            "pv=nrt": "La ecuación de estado de los gases ideales: PV = nRT.",
            "euler": "La identidad de Euler: e^{iπ} + 1 = 0, conecta cinco constantes matemáticas fundamentales.",
            "shannon": "La fórmula de la entropía de Shannon: H = -Σp(x)log₂p(x)",
            "bayes": "El teorema de Bayes: P(A|B) = P(B|A)·P(A)/P(B)",
            "schrodinger": "La ecuación de Schrödinger describe la evolución temporal de un sistema cuántico."
        }
        for eq, exp in ecuaciones_famosas.items():
            if eq.lower() in message.lower().replace(' ', ''):
                return exp
        # --- Para agregar más ecuaciones activas, seguir este patrón ---
        logicas_famosas = {
            "principio de no contradicción": "Aristóteles: Es imposible que algo sea y no sea al mismo tiempo y bajo el mismo aspecto.",
            "principio de identidad": "Leibniz: Todo objeto es idéntico a sí mismo.",
            "principio del tercero excluido": "Aristóteles: Entre el ser y el no ser no hay término medio.",
            "razón suficiente": "Leibniz: Nada ocurre sin una razón suficiente para que sea así y no de otro modo.",
            "máquina de turing": "Alan Turing: Un modelo abstracto de computación capaz de simular cualquier algoritmo computable.",
            "inteligencia artificial": "John McCarthy: La IA es la ciencia e ingeniería de hacer máquinas inteligentes."
        }
        for clave, explicacion in logicas_famosas.items():
            if clave in message.lower():
                return explicacion
        # 1b. Ecuaciones matemáticas simples
        eq_match = re.match(r"^([0-9\s\+\-\*/\(\)\.]+)$", message.strip())
        if eq_match:
            try:
                # Evalúa la expresión matemática de forma segura
                result = eval(eq_match.group(1), {"__builtins__": None}, {"math": math})
                return f"El resultado es: {result}"
            except Exception as e:
                return f"No pude calcular la expresión: {e}"
        # 2. Expresiones lógicas simples
        if any(op in message for op in [" and ", " or ", " not "]):
            try:
                result = eval(message, {"__builtins__": None})
                return f"El resultado lógico es: {result}"
            except Exception as e:
                return f"No pude evaluar la lógica: {e}"
        # 3. Solicitud de código
        if "código" in message.lower() or "programa" in message.lower():
            # Busca una palabra clave de algoritmo
            if "factorial" in message.lower():
                return "Aquí tienes un código en Python para calcular el factorial:\n\ndef factorial(n):\n    return 1 if n==0 else n*factorial(n-1)"
            if "búsqueda binaria" in message.lower():
                return "Código de búsqueda binaria en Python:\n\ndef busqueda_binaria(lista, objetivo):\n    izq, der = 0, len(lista)-1\n    while izq <= der:\n        mid = (izq + der) // 2\n        if lista[mid] == objetivo:\n            return mid\n        elif lista[mid] < objetivo:\n            izq = mid + 1\n        else:\n            der = mid - 1\n    return -1"
            # Plantilla genérica
            return "¿Qué código necesitas? Puedo generar ejemplos en Python si me das el algoritmo."
        # 4. Reconocimiento de claves conocidas
        claves = {"clave_secreta": "42-XYZ", "api_key": "DEMO-1234"}
        for k, v in claves.items():
            if k in message:
                return f"La clave '{k}' es: {v}"
        # 5. (Futuro) Detección de dibujos
        if any(word in message.lower() for word in ["dibuja", "grafica", "pinta"]):
            return "¡Puedo dibujar en el futuro! Esta función se autogestionará para soportar gráficos y dibujos en versiones posteriores."
        # Si no detecta nada especial
        return None

    # --- Módulos stub para autogestión futura ---
    def math_module(self, message: str) -> str:
        """
        Módulo matemático avanzado: cálculo real con sympy para derivadas, integrales, ecuaciones simbólicas, etc.
        """
        import sympy as sp
        import re
        # Derivada
        match_deriv = re.search(r'derivada de ([a-zA-Z0-9_\^\*\+\-\/\(\) ]+) ?(respecto a ([a-zA-Z]))?', message.lower())
        if match_deriv:
            expr = match_deriv.group(1)
            var = match_deriv.group(3) if match_deriv.group(3) else 'x'
            try:
                x = sp.symbols(var)
                deriv = sp.diff(expr, x)
                return f"La derivada de {expr} respecto a {var} es: {deriv}"
            except Exception as e:
                return f"Error al calcular derivada: {e}"
        # Integral
        match_integ = re.search(r'integral de ([a-zA-Z0-9_\^\*\+\-\/\(\) ]+) ?(respecto a ([a-zA-Z]))?', message.lower())
        if match_integ:
            expr = match_integ.group(1)
            var = match_integ.group(3) if match_integ.group(3) else 'x'
            try:
                x = sp.symbols(var)
                integ = sp.integrate(expr, x)
                return f"La integral de {expr} respecto a {var} es: {integ} + C"
            except Exception as e:
                return f"Error al calcular integral: {e}"
        # Ecuaciones simbólicas
        match_eq = re.search(r'resuelve (.+)=0', message.lower())
        if match_eq:
            eq = match_eq.group(1)
            try:
                x = sp.symbols('x')
                soluciones = sp.solve(eq, x)
                return f"Soluciones de {eq}=0: {soluciones}"
            except Exception as e:
                return f"Error al resolver ecuación: {e}"
        # Si no se reconoce la operación
        return "No pude identificar la operación matemática avanzada. Prueba con 'derivada de ...', 'integral de ...', o 'resuelve ...=0'"

    def transformer_module(self, message: str) -> str:
        """
        Módulo de procesamiento de lenguaje avanzado (LLM/transformer/BERT/GPT).
        Usa un modelo real vía API si la clave está configurada.
        """
        # Paso 1: Corrección ortográfica básica para mensajes mal escritos
        import difflib
        palabras_comunes = ["hola", "adiós", "cómo", "estás", "puedes", "ayudar", "gracias", "frondabrick", "quién", "eres", "qué", "hacer", "versión", "puedo", "hacer", "conversar", "función", "ecuación"]
        palabras = message.strip().split()
        corregidas = []
        for palabra in palabras:
            if palabra.lower() in palabras_comunes:
                corregidas.append(palabra)
            else:
                match = difflib.get_close_matches(palabra.lower(), palabras_comunes, n=1, cutoff=0.75)
                if match:
                    corregidas.append(match[0])
                else:
                    corregidas.append(palabra)
        mensaje_corregido = ' '.join(corregidas)
        # Paso 2: Procesamiento real con LLM si hay API Key
        # --- Configura tu API Key aquí ---
        OPENAI_API_KEY = None  # Pon aquí tu API Key de OpenAI o similar
        if OPENAI_API_KEY:
            try:
                import openai
                openai.api_key = OPENAI_API_KEY
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": mensaje_corregido}]
                )
                return completion.choices[0].message.content
            except Exception as e:
                return f"Error al consultar LLM externo: {e}"
        # Si no hay API Key, responde indicando que se requiere configuración
        return "[LLM real no configurado: por favor agrega tu API Key en el código para activar el procesamiento de lenguaje avanzado.]"

    def vision_module(self, message: str) -> str:
        """
        Módulo de visión artificial: análisis de imágenes, cámara, etc.
        """
        # TODO: Integrar OpenCV, PIL, modelos de visión, acceso a cámara, etc.
        # Ejemplo de integración plug-and-play:
        if 'vision' in self.modules:
            return self.modules['vision'](message)
        return "[Módulo de visión artificial en desarrollo: pronto podré analizar imágenes, mirar por la cámara y describir lo que veo.]"

    def audio_module(self, message: str) -> str:
        """
        Módulo de procesamiento de audio: reconocimiento de voz, síntesis, etc.
        """
        # TODO: Integrar speech-to-text, text-to-speech, análisis de audio, etc.
        return "[Módulo de audio en desarrollo: pronto podré escuchar y hablar.]"

    def robotics_module(self, message: str) -> str:
        """
        Módulo de robótica: control de actuadores, sensores, etc.
        """
        # TODO: Integrar control de hardware, sensores, actuadores, etc.
        return "[Módulo de robótica en desarrollo: pronto podré interactuar con el mundo físico.]"


    def forward(self, x):
        """
        Propagación hacia adelante de la red neuronal simple.
        """
        import numpy as np
        z1 = np.dot(x, self.W1) + self.b1
        a1 = np.tanh(z1)
        z2 = np.dot(a1, self.W2) + self.b2
        # Softmax para salida
        exp_scores = np.exp(z2 - np.max(z2))
        y_pred = exp_scores / np.sum(exp_scores)
        return y_pred

    def learn(self, input_text: str, output_text: str):
        """
        Aprende una nueva asociación entre entrada y salida usando un paso de entrenamiento supervisado (tipo perceptrón).
        """
        import numpy as np
        x = self.vectorize_input(input_text)
        y_true = self.vectorize_output(output_text)
        # Forward
        z1 = np.dot(x, self.W1) + self.b1
        a1 = np.tanh(z1)
        z2 = np.dot(a1, self.W2) + self.b2
        # Softmax para salida
        exp_scores = np.exp(z2 - np.max(z2))
        y_pred = exp_scores / np.sum(exp_scores)
        # Backpropagation (descenso de gradiente simple)
        lr = 0.01
        dz2 = y_pred - y_true
        dW2 = np.outer(a1, dz2)
        db2 = dz2
        da1 = np.dot(self.W2, dz2)
        dz1 = da1 * (1 - np.tanh(z1)**2)
        dW1 = np.outer(x, dz1)
        db1 = dz1
        # Actualizar pesos
        self.W2 -= lr * dW2
        self.b2 -= lr * db2
        self.W1 -= lr * dW1
        self.b1 -= lr * db1
        # Guardar en memoria
        self.memory.append((input_text, output_text))
        print(f"Frondabrick aprendió: '{input_text}' => '{output_text}'")

    def train(self, epochs: int = 10):
        """
        Entrena la red neuronal con todas las interacciones almacenadas en memoria.
        """
        for epoch in range(epochs):
            for input_text, output_text in self.memory:
                self.learn(input_text, output_text)
        print(f"Entrenamiento completado por {epochs} épocas.")

    def vectorize_input(self, text: str):
        """
        Convierte el texto de entrada en un vector de tamaño fijo.
        """
        import numpy as np
        tokens = text.lower().split()
        vec = np.zeros(self.input_size)
        for i, token in enumerate(tokens[:self.input_size]):
            idx = self.vocab.setdefault(token, len(self.vocab))
            vec[i] = idx / 100.0  # Normalización simple
        return vec

    def vectorize_output(self, text: str):
        """
        Convierte el texto de salida en un vector de tamaño fijo.
        """
        import numpy as np
        tokens = text.lower().split()
        vec = np.zeros(self.output_size)
        for i, token in enumerate(tokens[:self.output_size]):
            idx = self.output_vocab.setdefault(token, len(self.output_vocab))
            vec[i] = idx / 100.0
        return vec

    def decode_output(self, vec):
        """
        Convierte un vector de salida en texto (respuesta).
        """
        import numpy as np
        if not self.output_vocab:
            return ""
        idx_to_token = {v: k for k, v in self.output_vocab.items()}
        tokens = []
        for v in vec:
            idx = int(round(v * 100))
            token = idx_to_token.get(idx, "")
            if token:
                tokens.append(token)
        return " ".join(tokens)

# Ejemplo de uso (esto no se ejecutaría directamente aquí en producción)
if __name__ == "__main__":
    core = FrondaBrick()
    test_response = core.process_message("test_client_123", "hola fronda")
    print(f"Respuesta de prueba: {test_response}")
    core.learn("Los gatos tienen cuatro patas.", source_client="test_client_123")

