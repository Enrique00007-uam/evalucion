from pila import invertir_palabras_frase, Pila

"""
Función principal que maneja el menú y la interacción.
Permite al usuario ingresar una frase para invertir sus palabras o salir del programa.
"""

#Muestra el menú de opciones

def mostrar_menu():
    print("--- Menú Ejercicio #1: Inversión de Palabras ---")
    print("1. Ingresar frase para invertir")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            frase = input("Ingrese la frase: ")
            if frase:
                frase_invertida = invertir_palabras_frase(frase)
                print(f"Frase original: {frase}")
                print(f"Frase invertida: {frase_invertida}")
            else:
                print("La frase no puede estar vacía.")
        elif opcion == '2':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


main() 
