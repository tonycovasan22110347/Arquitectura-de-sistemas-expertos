class SistemaExpertoPlanta:
    def __init__(self):
        # Representación del conocimiento: hechos sobre el estado de la planta
        self.hechos = set()
        
        # Representación del conocimiento: reglas de diagnóstico
        self.reglas = [
            {"condiciones": {("hojas_amarillas", True), ("raices_sucias", True)}, "diagnostico": "La planta necesita más agua y limpieza de raíces."},
            {"condiciones": {("hojas_amarillas", True), ("exceso_sol", True)}, "diagnostico": "La planta está recibiendo demasiado sol, cambiarla a sombra."},
            {"condiciones": {("hojas_seca", True), ("falta_riego", True)}, "diagnostico": "La planta necesita riego urgente."},
            {"condiciones": {("hojas_verde_sanas", True)}, "diagnostico": "La planta está saludable."},
        ]

    def agregar_hecho(self, hecho):
        """Agregar un hecho al conjunto de hechos."""
        self.hechos.add(hecho)

    def diagnosticar(self):
        """Aplica las reglas para diagnosticar el estado de la planta."""
        for regla in self.reglas:
            if regla["condiciones"].issubset(self.hechos):  # Comparar los hechos con las condiciones de las reglas
                return regla["diagnostico"]
        return "No se puede diagnosticar el problema con los hechos disponibles."

    def realizar_diagnostico(self):
        """Recopila hechos sobre la planta y hace un diagnóstico."""
        print("Sistema experto de diagnóstico de planta.")
        
        # Simulación de adquisición de hechos
        self.agregar_hecho(("hojas_amarillas", True))
        self.agregar_hecho(("raices_sucias", True))

        # Diagnóstico basado en los hechos
        diagnostico = self.diagnosticar()
        print(f"Diagnóstico: {diagnostico}")


# Crear una instancia del sistema experto
sistema_planta = SistemaExpertoPlanta()

# Ejecutar el proceso de diagnóstico de la planta
sistema_planta.realizar_diagnostico()
