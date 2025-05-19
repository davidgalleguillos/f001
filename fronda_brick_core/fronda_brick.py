# fronda_brick_core/fronda_brick.py

# Import persistence and learning modules when they are defined
# from .persistencia import crud as persistence_module
# from .modulos import aprendizaje

class FrondaBrick:
    def __init__(self):
        """
        Inicializa el núcleo de Frondabrick con una red neuronal simple y memoria de entrenamiento.
        """
        self.memory = []  # Memoria de interacciones (input, output)
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

    def process_message(self, client_id: str, message: str) -> str:
        """
        Procesa un mensaje entrante y devuelve una respuesta generada por la red neuronal.
        Si no reconoce el patrón, responde que está aprendiendo.
        """
        print(f"Núcleo recibió de {client_id}: {message}")
        x = self.vectorize_input(message)
        y_pred = self.forward(x)
        response = self.decode_output(y_pred)
        if response.strip() == "":
            response = "Aún estoy aprendiendo. ¿Puedes explicarme mejor o darme ejemplos?"
        # Guardar interacción para entrenamiento futuro
        self.memory.append((message, response))
        print(f"Núcleo responde a {client_id}: {response}")
        return response

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

