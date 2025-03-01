class SistemaExpertoSalud:
    def __init__(self):
        # Representación del conocimiento: síntomas y enfermedades posibles
        self.enfermedades = {
            "gripe": {"fiebre": True, "tos": True, "dolor_cabeza": False},
            "resfriado": {"fiebre": False, "tos": True, "dolor_cabeza": False},
            "migraña": {"fiebre": False, "tos": False, "dolor_cabeza": True},
        }
    
    def diagnosticar(self, sintomas):
        """Utiliza el conocimiento para diagnosticar la enfermedad según los síntomas."""
        for enfermedad, sintomas_enfermedad in self.enfermedades.items():
            if sintomas == sintomas_enfermedad:
                return f"La persona tiene {enfermedad}."
        return "No se puede diagnosticar con los síntomas proporcionados."
    
    def utilizar_conocimiento(self):
        """Simula la recopilación de síntomas y realiza un diagnóstico."""
        print("Sistema experto de diagnóstico de salud.")
        
        # Simulación de los síntomas de la persona
        sintomas_persona = {"fiebre": True, "tos": True, "dolor_cabeza": False}
        
        # Diagnóstico basado en los síntomas
        diagnostico = self.diagnosticar(sintomas_persona)
        print(f"Diagnóstico: {diagnostico}")

# Crear una instancia del sistema experto
sistema_salud = SistemaExpertoSalud()

# Ejecutar el diagnóstico
sistema_salud.utilizar_conocimiento()
