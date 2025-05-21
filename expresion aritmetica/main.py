import os
import expresion_aritmetica as ea
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menú principal del programa
def menu():
    limpiar_pantalla()
    while True:
        print("\n--- CONVERTIDOR DE EXPRESIONES INFJIAS A POSTFIJAS ---")
        print("1. Ingresar expresión con letras (por ejemplo: A+B*C)")
        print("2. Ingresar expresión con números (por ejemplo: 3+4*2)")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-4): ")
        
        limpiar_pantalla()
        

        if opcion == '1':
            expr = input("Ingrese la expresión con letras: ").replace(" ", "")
            postfija = ea.infija_a_postfija(expr)
            print("Postfija:", ' '.join(postfija))

        elif opcion == '2':
            expr = input("Ingrese la expresión con números: ").replace(" ", "")
            postfija = ea.infija_a_postfija(expr)
            print("Postfija:", ' '.join(postfija))

            calcular = input("¿Desea calcular el resultado? (s/n): ").lower()
            if calcular == 's':
                resultado = ea.evaluar_postfija(postfija)
                print("Resultado:", resultado)

        elif opcion == '3':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            
        input("\nPresione ENTER para continuar...")


menu()
