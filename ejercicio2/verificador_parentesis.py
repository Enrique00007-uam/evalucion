"""Ejercicio #2: Verificación de paréntesis balanceados. Escriba un programa que
determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ] balanceados.
Use una pila para realizar el seguimiento de los paréntesis abiertos.
"""

# Nodo para la lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Pila (Stack) implementation usando listas enlazadas
class Pila:
    def __init__(self):
        self._cima_nodo = None  # Apunta al nodo superior de la pila

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
        return None

    def cima(self):
        if not self.esta_vacia():
            return self._cima_nodo.valor
        return None

# funcion para verificar los parentesis
def verificar_parentesis_balanceados(cadena):
    """
    Verifica si una cadena de texto tiene los paréntesis (), {}, y [] balanceados.
    """
    pila = Pila()
    mapa_parentesis = { ")": "(",
                        "}": "{",
                        "]": "["}

    for caracter in cadena:
        if caracter in "([{":
            pila.apilar(caracter)
        elif caracter in "])}":
            if pila.esta_vacia():
                return False  # Cierre sin apertura
            if pila.cima() == mapa_parentesis[caracter]:
                pila.desapilar()
            else:
                return False # Desbalanceado
    
    return pila.esta_vacia() # Si la pila está vacía, están balanceados
