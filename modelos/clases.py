class Estuidantes:

    def __init__(self, nombres, apellidos, carrera, promedio):
        self.nombres = nombres
        self.apellidos = apellidos
        self.carrera = carrera
        self.promedio = promedio

        def __str__(self):
            return f"Datos del estudiante \n Nombre completo: {self.nombres} {self.apellidos} \n Carrera: {self.carrera} \n Promedio : {self.promedio}"
        
