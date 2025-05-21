from lista_enlazada import ListaEnlazada

def mostrar_menu():
    print("\n--- Menú Ejercicio #5: Búsqueda en Lista Enlazada ---")
    print("1. Agregar elemento a la lista")
    print("2. Buscar elemento en la lista")
    print("3. Mostrar lista actual")
    print("4. Salir")

def main():
    lista = ListaEnlazada()

    # Agregar algunos elementos iniciales
    lista.agregar_al_final(10)
    lista.agregar_al_final("veinte")
    lista.agregar_al_final(30.5)
    lista.agregar_al_final("cuarenta")

    while True:
        print(f"\n{lista.mostrar_lista()}")
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            valor_str = input("Ingrese el valor a agregar (se guardará como texto): ") 
            if valor_str: # Asegurarse que no sea una cadena vacía
                # Todos los valores se guardan como string directamente
                lista.agregar_al_final(valor_str) 
            else:
                print("El valor no puede estar vacío.")
        
        elif opcion == '2':
            valor_buscado_str = input("Ingrese el valor a buscar: ")
            if valor_buscado_str:
                # La función buscar_valor ya maneja la comparación como string si es necesario
                resultado_busqueda = lista.buscar_valor(valor_buscado_str)
                print(resultado_busqueda)
            else:
                print("El valor a buscar no puede estar vacío.")

        elif opcion == '3':
            # Se muestra al inicio del bucle, llamando  al método
            print(f"Mostrando lista: {lista.mostrar_lista()}")

        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


main()
