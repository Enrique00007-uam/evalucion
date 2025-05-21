from cola_prioridad import ColaPrioridad # ElementoPrioridad no es necesario importar aquí

def mostrar_menu():
    print("\n--- Menú Ejercicio #4: Cola de Prioridad ---")
    print("1. Agregar elemento") # Actualizado texto del menú
    print("2. Atender siguiente elemento (desencolar)")
    print("3. Ver siguiente elemento (sin desencolar)")
    print("4. Mostrar cola actual")
    print("5. Salir")

def main():
    cola_p = ColaPrioridad()

    # Ejemplos iniciales
    cola_p.agregar("Tarea Urgente A", 1) # Renombrado de encolar a agregar
    cola_p.agregar("Tarea Normal", 5) # Renombrado de encolar a agregar
    cola_p.agregar("Tarea Poco Urgente", 10) # Renombrado de encolar a agregar
    cola_p.agregar("Tarea Urgente B", 1) # Renombrado de encolar a agregar

    while True:
        print(f" \n {str(cola_p)}")
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del elemento: ")
            while True:
                try:
                    prioridad_str = input(f"Ingrese la prioridad para '{nombre}' (entero positivo, menor es más prioritario): ")
                    prioridad = int(prioridad_str)
                    if prioridad <= 0:
                        print("La prioridad debe ser un número entero positivo.")
                        continue
                    break
                except ValueError:
                    print("Prioridad no válida. Debe ser un número entero.")
            
            if nombre:
                cola_p.agregar(nombre, prioridad) # Renombrado de encolar a agregar
            else:
                print("El nombre del elemento no puede estar vacío.")

        elif opcion == '2':
            elemento_atendido = cola_p.desencolar()
            if elemento_atendido:
                print(f"Elemento atendido: {elemento_atendido.nombre} con prioridad {elemento_atendido.prioridad}")
            else:
                print("La cola de prioridad está vacía. No hay elementos para atender.")
        
        elif opcion == '3':
            siguiente = cola_p.ver_siguiente()
            if siguiente:
                print(f"Siguiente elemento a atender: {siguiente.nombre} con prioridad {siguiente.prioridad}")
            else:
                print("La cola de prioridad está vacía.")

        elif opcion == '4':
            # Se muestra al inicio del bucle
            print("Mostrando cola (ya visible arriba del menú).")

        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
