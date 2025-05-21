"""Ejercicio #3: Simulación de una lista de reproducción de música. Implemente
una lista de reproducción de música utilizando una lista enlazada. El programa debe
permitir agregar canciones, eliminar canciones, reproducir la siguiente canción,
reproducir la canción anterior y mostrar la lista de reproducción actual."""

class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def __str__(self): 
        return f"'{self.titulo}' por {self.artista}" # si se le hase print() a una cancion se va a mostar este mensaje

class Nodo:  
    def __init__(self, cancion=None):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None # Nodo de la canción actualmente "reproduciéndose"

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_cancion(self, titulo, artista):
        nueva_cancion = Cancion(titulo, artista)
        nuevo_nodo = Nodo(nueva_cancion)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.actual = nuevo_nodo # La primera canción es la actual
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        print(f"Canción {str(nueva_cancion)} agregada.")

    def eliminar_cancion(self, titulo_cancion):
        if self.esta_vacia():
            print("La lista de reproducción está vacía.")
            return

        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.cancion.titulo.lower() == titulo_cancion.lower():
                # Si es la canción actual, se mueve actual antes de eliminar
                if self.actual == nodo_actual:
                    if nodo_actual.siguiente:
                        self.actual = nodo_actual.siguiente
                    elif nodo_actual.anterior:
                        self.actual = nodo_actual.anterior
                    else: # Era la única canción
                        self.actual = None
                
                # Lógica de eliminación de nodo en lista
                if nodo_actual.anterior:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                else: # Es la cabeza
                    self.cabeza = nodo_actual.siguiente
                
                if nodo_actual.siguiente:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                else: # Es la cola
                    self.cola = nodo_actual.anterior
                
                # Si la lista queda vacía después de eliminar
                if self.cabeza is None:
                    self.cola = None
                    self.actual = None

                print(f"Canción '{titulo_cancion}' eliminada.")
                return
            nodo_actual = nodo_actual.siguiente
        print(f"Canción: {titulo_cancion} no encontrada.")

    def reproducir_siguiente(self):
        if not self.actual:
            if not self.esta_vacia(): # Si hay canciones pero ninguna es actual, reproducir la primera
                 self.actual = self.cabeza
                 print(f"Reproduciendo: {str(self.actual.cancion)}")
                 return
            print("No hay canción actual o la lista está vacía.")
            return
        if self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Reproduciendo siguiente: {str(self.actual.cancion)}")
        else:
            print("Ya estás en la última canción.")
            if self.actual:
                 print(f"Sigues reproduciendo: {str(self.actual.cancion)}")


    def reproducir_anterior(self):
        if not self.actual:
            if not self.esta_vacia(): # Si hay canciones pero ninguna es actual, reproducir la primera o última
                 self.actual = self.cabeza 
                 print(f"Reproduciendo: {str(self.actual.cancion)}")
                 return
            print("No hay canción actual o la lista está vacía.")
            return
        if self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Reproduciendo anterior: {str(self.actual.cancion)}")
        else:
            print("Ya estás en la primera canción.")
            if self.actual:
                 print(f"Sigues reproduciendo: {str(self.actual.cancion)}")


    def mostrar_lista_actual(self):
        if self.esta_vacia():
            print("La lista de reproducción está vacía.")
            return
        
        print("--- Lista de Reproducción Actual ---")
        nodo_temp = self.cabeza
        idx = 1
        while nodo_temp:
            prefijo = "  "
            if nodo_temp == self.actual:
                prefijo = "► "
            print(f"{prefijo}{idx}. {str(nodo_temp.cancion)}")
            nodo_temp = nodo_temp.siguiente
            idx += 1
        if not self.actual and not self.esta_vacia():
             print(" (Ninguna canción seleccionada para reproducir)")
        elif self.actual:
            print(f"\nReproduciendo actualmente: {str(self.actual.cancion)}")
