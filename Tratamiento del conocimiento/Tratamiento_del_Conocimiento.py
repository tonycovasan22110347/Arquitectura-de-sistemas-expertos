class SistemaExpertoMaquina:
    def __init__(self):
        # Representación inicial del conocimiento: hechos sobre el estado de la máquina
        self.hechos = set()
        
        # Reglas de diagnóstico iniciales
        self.reglas = [
            {"condiciones": {("motor_fallando", True), ("temperatura_alta", True)}, "diagnostico": "El motor está fallando debido a sobrecalentamiento."},
            {"condiciones": {("ruido_excesivo", True), ("vibracion_alta", True)}, "diagnostico": "Posible fallo en el sistema de rodamientos o en los ejes."},
            {"condiciones": {("sensor_falla", True)}, "diagnostico": "El sensor de temperatura está fallando."},
            {"condiciones": {("falta_aceite", True)}, "diagnostico": "La máquina necesita aceite."},
        ]
    
    def agregar_hecho(self, hecho):
        """Agregar un hecho al conjunto de hechos."""
        self.hechos.add(hecho)
    
    def actualizar_reglas(self):
        """Modificar las reglas basadas en nuevo conocimiento."""
        print("Actualizando reglas debido a nuevo conocimiento...")
        nueva_regla = {"condiciones": {("motor_fallando", True), ("falta_aceite", True)}, "diagnostico": "El motor está fallando por falta de lubricación. Se necesita aceite."}
        self.reglas.append(nueva_regla)
    
    def diagnosticar(self):
        """Aplica las reglas para diagnosticar el estado de la máquina."""
        for regla in self.reglas:
            if regla["condiciones"].issubset(self.hechos):  # Comparar los hechos con las condiciones de las reglas
                return regla["diagnostico"]
        return "No se puede diagnosticar el problema con los hechos disponibles."

    def realizar_diagnostico(self):
        """Recopila hechos sobre la máquina y hace un diagnóstico."""
        print("Sistema experto de diagnóstico de fallos en la máquina.")
        
        # Simulación de adquisición de hechos
        self.agregar_hecho(("motor_fallando", True))
        self.agregar_hecho(("temperatura_alta", True))

        # Diagnóstico basado en los hechos
        diagnostico = self.diagnosticar()
        print(f"Diagnóstico inicial: {diagnostico}")
        
        # Actualización del conocimiento: Se aprende que falta aceite
        self.agregar_hecho(("falta_aceite", True))
        
        # Actualización de reglas: Aprendemos sobre la falta de aceite afectando al motor
        self.actualizar_reglas()
        
        # Hacer un diagnóstico nuevamente después de actualizar el conocimiento
        print("\nReevaluando diagnóstico después de actualización del conocimiento:")
        diagnostico_actualizado = self.diagnosticar()
        print(f"Diagnóstico actualizado: {diagnostico_actualizado}")


# Crear una instancia del sistema experto
sistema_maquina = SistemaExpertoMaquina()

# Ejecutar el proceso de diagnóstico de la máquina
sistema_maquina.realizar_diagnostico()
