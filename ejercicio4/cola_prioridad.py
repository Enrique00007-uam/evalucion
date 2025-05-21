"""Ejercicio #4: Implementación de una cola de prioridad. Diseñe una cola de
prioridad donde los elementos se desencolan según su prioridad. Cada elemento
tendrá un nombre y una prioridad (un número entero, donde un número menor indica
mayor prioridad)."""

class ElementoPrioridad:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad


    def __lt__(self, otro):
        if self.prioridad == otro.prioridad:
           
            return self.nombre < otro.nombre 
        return self.prioridad < otro.prioridad

    def __str__(self):
        return f"({self.nombre}, Prioridad: {self.prioridad})" #si se le hase print a un ElementoPrioridad muestra ese mensaje

class Nodo:
    def __init__(self, elemento_prioridad):
        self.elemento = elemento_prioridad # Almacena un objeto ElementoPrioridad
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.cabeza = None # Cabeza de la lista enlazada

    def esta_vacia(self):
        return self.cabeza is None

    def agregar(self, nombre, prioridad): # Renombrado de encolar a agregar
        """
        Agrega un elemento a la cola (lista enlazada ordenada) con su nombre y prioridad.
        Un número menor indica mayor prioridad.
        Mantiene el orden FIFO para elementos con la misma prioridad.
        """
        elemento_nuevo = ElementoPrioridad(nombre, prioridad)
        nuevo_nodo = Nodo(elemento_nuevo)

        # Caso 1: La lista está vacía o el nuevo nodo tiene mayor prioridad que la cabeza
        if self.esta_vacia() or elemento_nuevo.prioridad < self.cabeza.elemento.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            # Caso 2: Insertar en medio o al final de la lista
            actual = self.cabeza
            # Avanzar mientras el siguiente nodo exista y 
            # la prioridad del nuevo elemento sea mayor o igual 
            # (para insertar después y mantener FIFO para prioridades iguales)
            while actual.siguiente is not None and \
                  elemento_nuevo.prioridad >= actual.siguiente.elemento.prioridad:
                actual = actual.siguiente
            
            # Insertar el nuevo nodo después de 'actual'
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            
        print(f"Elemento {str(elemento_nuevo)} agregado.") # Actualizado mensaje


    def desencolar(self):
        """
        Elimina y devuelve el elemento con la mayor prioridad (menor número) de la cabeza.
        """
        if self.esta_vacia():
            return None
        elemento_desencolado = self.cabeza.elemento
        self.cabeza = self.cabeza.siguiente
        return elemento_desencolado

    def ver_siguiente(self):
        if self.esta_vacia():
            return None
        return self.cabeza.elemento
    
    def __str__(self):
        if self.esta_vacia():
            return "Cola de Prioridad: (vacía)"
        
        elementos_str = []
        actual = self.cabeza
        while actual:
            elementos_str.append(str(actual.elemento))
            actual = actual.siguiente
        return "Cola de Prioridad (de mayor a menor prioridad): \n  " + "\n  ".join(elementos_str)

