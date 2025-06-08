import modelos.clases as m
import dao.operaciones as o 
import os 

lista = o.EstudianteDao()

def menu():
    os.system('cls || clear')
    print("""""
1. Agregar
2. Mostrar
3. Salir
Digite la opcion a realizar : """)

def agregar():
    os.system('cls || clear')
    print("Digite los siguientes datos : ")
    nombre = input("Nombres : ")
    apellido = input("Apellidos : ")
    carrera = input("Carrera : ")
    promedio = int(input("Promedio : "))
    estudiante = m.Estudiantes(nombre, apellido, carrera, promedio)
    lista.agregar(estudiante)

def mostrar():
    os.system('cls || clear')
    print("Lista de estudiantes : ")
    for est in lista.mostrar():
        print(est)

def main():
    while(True):
        menu()
        opcion = input()
        if opcion == "1":
            agregar()
        elif opcion == "2":
            mostrar()
        elif opcion == "3":
          print("Saliendo del programa...")
          break
        else:
            print("Opcion no valida, intente de nuevo.")

