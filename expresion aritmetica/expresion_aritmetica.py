import os  # Para limpiar la terminal según el sistema operativo

def es_operador(c):
    return c in "+-*/^"

# Retorna la precedencia de un operador
def precedencia(c):
    if c == '+' or c == '-':
        return 1
    elif c == '*' or c == '/':
        return 2
    elif c == '^':
        return 3
    else:
        return 0

# Convierte una expresión infija a postfija (notación polaca inversa)
def infija_a_postfija(expresion):
    pila = []       # Pila para operadores
    postfija = []   # Lista para la expresión postfija
    i = 0

    while i < len(expresion):
        simbolo = expresion[i]

        if simbolo.isalnum():  # Letras o números
            if simbolo.isdigit():
                numero = simbolo
                while i + 1 < len(expresion) and expresion[i + 1].isdigit():
                    i += 1
                    numero += expresion[i]
                postfija.append(numero)
            else:
                postfija.append(simbolo)
        elif simbolo == '(':
            pila.append(simbolo)
        elif simbolo == ')':
            while pila and pila[-1] != '(':
                postfija.append(pila.pop())
            pila.pop()  # Quita el paréntesis de apertura '('
        elif es_operador(simbolo):
            while (pila and pila[-1] != '(' and
                   precedencia(simbolo) <= precedencia(pila[-1])):
                postfija.append(pila.pop())
            pila.append(simbolo)
        i += 1

    while pila:
        postfija.append(pila.pop())

    return postfija  # Se devuelve una lista de tokens

# Evalúa una expresión postfija numérica
def evaluar_postfija(postfija):
    pila = []

    for token in postfija:
        if token.isdigit():
            pila.append(int(token))
        elif token in "+-*/^":
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)
            elif token == '^':
                pila.append(a ** b)
    return pila[0] if pila else None
