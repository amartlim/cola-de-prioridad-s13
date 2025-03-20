import heapq  # Importamos heapq para manejar la cola de prioridad

# Definimos la clase Paciente con nombre, enfermedad y nivel de urgencia
class Paciente:
    def __init__(self, nombre, enfermedad, urgencia):
        self.nombre = nombre  # Nombre del paciente
        self.enfermedad = enfermedad  # Enfermedad del paciente
        self.urgencia = urgencia  # Nivel de urgencia (1 crítico - 5 leve)
    
    def __lt__(self, otro):  # Método para comparar pacientes por urgencia
        return self.urgencia < otro.urgencia  # Menor número = mayor prioridad

    def __repr__(self):  # Método para representar un paciente como texto
        return f"{self.nombre} - {self.enfermedad} (Urgencia: {self.urgencia})"

# Definimos la clase SalaEmergencias para gestionar la cola de prioridad
class SalaEmergencias:
    def __init__(self):
        self.cola_prioridad = []  # Lista para la cola de prioridad
    
    def agregar_paciente(self, nombre, enfermedad, urgencia):
        heapq.heappush(self.cola_prioridad, Paciente(nombre, enfermedad, urgencia))  # Agregamos a la cola
        print(f"Paciente {nombre} con {enfermedad} agregado con urgencia {urgencia}.")
    
    def atender_paciente(self):
        if self.cola_prioridad:
            print(f"Atendiendo a {heapq.heappop(self.cola_prioridad)}")
        else:
            print("No hay pacientes en espera.")

    def mostrar_pacientes(self):
        print("Pacientes en espera:", self.cola_prioridad)

# Diccionario con enfermedades y sus niveles de urgencia
urgencias = {
    "Ataque al corazón": 1,
    "Fractura grave": 2,
    "Fiebre alta": 3,
    "Corte profundo": 3,
    "Dolor de cabeza": 5,
    "Resfriado": 5
}

# Ejemplo de uso de la sala de emergencias
sala = SalaEmergencias()
sala.agregar_paciente("Juan", "Fiebre alta", urgencias["Fiebre alta"])  # Urgencia 3
sala.agregar_paciente("María", "Ataque al corazón", urgencias["Ataque al corazón"])  # Urgencia 1
sala.agregar_paciente("Carlos", "Resfriado", urgencias["Resfriado"])  # Urgencia 5
sala.agregar_paciente("Ana", "Fractura grave", urgencias["Fractura grave"])  # Urgencia 2

sala.mostrar_pacientes()  # Mostramos la lista de pacientes en espera

print("Atendiendo pacientes en orden de prioridad:")
while sala.cola_prioridad:
    sala.atender_paciente()