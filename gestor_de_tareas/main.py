import os
import platform

from tareas import GestorDeTareas, TareaProgramada, TareaRecurrente

def limpiar_pantalla():
    """Limpiar la pantalla según el sistema operativo"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menu():
    print("\nMenú:\n ")
    print("1. Crear una tarea")
    print("2. Consultar tareas")
    print("3. Actualizar estado")
    print("4. Borrar una tarea")
    print("5. Salir")

def main():
    gestor = GestorDeTareas()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            detalle = input("Detalle: ")
            gestor.crear_tarea(titulo, detalle)
        elif opcion == "2":
            gestor.leer_tareas()
        elif opcion == "3":
            titulo = input("Título de la tarea a actualizar: ")
            nuevo_estado = input("Ingrese el nuevo estado (pendiente, en progreso, completa): ")
            gestor.actualizar_tarea(titulo, nuevo_estado)
        elif opcion == "4":
            titulo = input("Título de la tarea a borrar: ")
            gestor.borrar_tarea(titulo)
        elif opcion == "5":
            print("Ha finalizado el sistema ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")

if __name__ == "__main__":
    main()
