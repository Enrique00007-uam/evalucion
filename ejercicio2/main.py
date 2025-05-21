from verificador_parentesis import verificar_parentesis_balanceados

def mostrar_menu():
    print("\n--- Menú Ejercicio #2: Verificación de Paréntesis Balanceados ---")
    print("1. Ingresar cadena para verificar")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cadena = input("Ingrese la cadena de texto con paréntesis: ")
            if verificar_parentesis_balanceados(cadena):
                print(f"La cadena {cadena} tiene los paréntesis balanceados.")
            else:
                print(f"La cadena {cadena} NO tiene los paréntesis balanceados.")
        elif opcion == '2':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


main()
