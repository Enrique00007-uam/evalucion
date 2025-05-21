"""✓ Ejercicio #1: Inversión de palabras en una frase. Desarrolle un programa que
utilice una pila para invertir el orden de las palabras en una frase dada. Por ejemplo,
la frase "Hola mundo desde UAM" debería invertirse a "UAM desde mundo Hola"."""

# Nodo para la lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Pila (Stack) implementation usando listas enlazadas
class Pila:
    def __init__(self):
        self._cima_nodo = None  # Cambiamos _items por _cima_nodo que apunta al nodo superior

    def esta_vacia(self):
        return self._cima_nodo is None

    def apilar(self, item):
        nuevo_nodo = Nodo(item)
        nuevo_nodo.siguiente = self._cima_nodo
        self._cima_nodo = nuevo_nodo

    def desapilar(self):
        if not self.esta_vacia():
            valor_desapilado = self._cima_nodo.valor
            self._cima_nodo = self._cima_nodo.siguiente
            return valor_desapilado
        return None # devuelve dato vacio si no hay elementos en la pila

    def cima(self):
        if not self.esta_vacia():
            return self._cima_nodo.valor
        return None

# funcion para revertir la palabra Invierte el orden de las palabras en una frase utilizando una pila.
    
def invertir_palabras_frase(frase):
   
    palabras = frase.split() # Divide la frase en una lista de palabras
    pila_palabras = Pila()

    for palabra in palabras:
        pila_palabras.apilar(palabra)

    frase_invertida = []
    while not pila_palabras.esta_vacia():
        frase_invertida.append(pila_palabras.desapilar())

    return " ".join(frase_invertida) #cadena con todas las palabras invertidas separados con un espacio
