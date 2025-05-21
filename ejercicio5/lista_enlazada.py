"""Ejercicio #5: Búsqueda en una lista enlazada. Cree una función que busque un
valor específico en una lista enlazada. La función debe devolver la posición del valor
si se encuentra, o un mensaje indicando que el valor no está en la lista."""

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return str(self.valor)

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            print(f"Valor '{valor}' agregado a la lista (como cabeza).")
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        print(f"Valor '{valor}' agregado al final de la lista.")

    def buscar_valor(self, valor_buscado):
        """
        Busca un valor específico en la lista enlazada.
        Devuelve la posición (basada en 1) si se encuentra, o un mensaje.
        """
        if self.esta_vacia():
            return "La lista está vacía. No se puede buscar."

        actual = self.cabeza
        posicion = 0
        while actual:
            # Convertimos ambos a string para una comparación más flexible si los tipos pueden variar
            if str(actual.valor) == str(valor_buscado):
                return f"Valor '{valor_buscado}' encontrado en la posición {posicion}."
            actual = actual.siguiente
            posicion += 1
        
        return f"Valor '{valor_buscado}' no encontrado en la lista."

    def mostrar_lista(self): 
        if self.esta_vacia():
            return "Lista: (vacía)"
        
        resultado_str = "Lista: "
        actual = self.cabeza
        while actual:
            resultado_str += str(actual.valor)
            if actual.siguiente:
                resultado_str += " -> "
            actual = actual.siguiente
        return resultado_str

