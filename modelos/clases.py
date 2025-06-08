class Estudiantes:

    def __init__(self, nombres, apellidos, carrera, promedio):
        self.nombres = nombres
        self.apellidos = apellidos
        self.carrera = carrera
        self.promedio = promedio

        def __str__(self):
            return(f"\nDatos del estudiante\nNombre completo: {self.nombres} {self.apellidos} \nCarrera: {self.carrera} \nPromedio: {self.promedio}")
        
