from lista_reproduccion import ListaReproduccion

def mostrar_menu():
    print("\n--- Menú Ejercicio #3: Lista de Reproducción de Música ---")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Reproducir siguiente canción")
    print("4. Reproducir canción anterior")
    print("5. Mostrar lista de reproducción actual")
    print("6. Salir")

def main():
    playlist = ListaReproduccion()

   
    playlist.agregar_cancion("Bohemian Rhapsody", "Queen")



    while True:
        
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título de la canción: ")
            artista = input("Ingrese el artista de la canción: ")
            if titulo and artista:
                playlist.agregar_cancion(titulo, artista)
            else:
                print("Título y artista no pueden estar vacíos.")
        elif opcion == '2':
            titulo = input("Ingrese el título de la canción a eliminar: ")
            playlist.eliminar_cancion(titulo)
        elif opcion == '3':
            playlist.reproducir_siguiente()
        elif opcion == '4':
            playlist.reproducir_anterior()
        elif opcion == '5':
            print("Mostrando lista.")
            playlist.mostrar_lista_actual()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()
