class SistemaExpertoBebidas:
    def __init__(self):
        self.respuestas = {}  # Almacena las respuestas del usuario

    def hacer_pregunta(self, pregunta):
        """Hace preguntas al usuario y almacena las respuestas."""
        respuesta = input(pregunta + " (frio/calor): ").strip().lower()
        self.respuestas[pregunta] = respuesta
        return respuesta

    def recomendar_bebida(self):
        """Basado en las respuestas, recomienda una bebida."""
        if self.respuestas.get("¿Hace calor?") == "calor":
            return "Te recomiendo una bebida fría, como un té helado o jugo."
        elif self.respuestas.get("¿Hace frío?") == "frio":
            return "Te recomiendo una bebida caliente, como un café o chocolate caliente."
        else:
            return "No puedo determinar la temperatura. ¿Podrías decirme si hace calor o frío?"

    def realizar_recomendacion(self):
        """Interactúa con el usuario para hacer la recomendación."""
        print("Bienvenido al sistema experto de recomendación de bebidas.")
        
        self.hacer_pregunta("¿Hace calor?")
        self.hacer_pregunta("¿Hace frío?")
        
        recomendacion = self.recomendar_bebida()
        print("\nRecomendación:", recomendacion)


# Crear una instancia del sistema experto
sistema_bebidas = SistemaExpertoBebidas()

# Ejecutar el proceso de recomendación
sistema_bebidas.realizar_recomendacion()
