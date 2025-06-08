class EstudianteDao:
#data access object
#DAO
        def __init__(self):
            self.estudiantes = []   

        def agregar(self, estudiante):
            self.estudiantes.append(estudiante)
        
        def mostrar(self):
            return self.estudiantes
    
        def calcular_beca(self):
            return self.estudiantes
