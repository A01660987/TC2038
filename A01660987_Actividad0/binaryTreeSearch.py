import random

class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if not self.raiz:
            self.raiz = Nodo(dato)
            return 1
        else:
            return self._insertar(dato, self.raiz, 1)

    def _insertar(self, dato, nodo, n):
        if dato < nodo.dato:
            if not nodo.izquierda:
                nodo.izquierda = Nodo(dato)
                return n + 1
            else:
                return self._insertar(dato, nodo.izquierda, n + 1)
        elif dato > nodo.dato:
            if not nodo.derecha:
                nodo.derecha = Nodo(dato)
                return n + 1
            else:
                return self._insertar(dato, nodo.derecha, n + 1)
        else:
            return n + 1

tamaño = 10
lista = [*range(1, tamaño + 1)]
lista = random.sample(lista, len(lista))
arbol = Arbol()

for i in lista:
    arbol.insertar(i)

print("Tamaño: " + str(tamaño) + " Pasos: " + str(arbol.insertar(11)))

tamaño = 100
lista = [*range(1, tamaño + 1)]
lista = random.sample(lista, len(lista))
arbol = Arbol()

for i in lista:
    arbol.insertar(i)

print("Tamaño: " + str(tamaño) + " Pasos: " + str(arbol.insertar(101)))

tamaño = 1000
lista = [*range(1, tamaño + 1)]
lista = random.sample(lista, len(lista))
arbol = Arbol()

for i in lista:
    arbol.insertar(i)

print("Tamaño: " + str(tamaño) + " Pasos: " + str(arbol.insertar(1001)))

tamaño = 10000
lista = [*range(1, tamaño + 1)]
lista = random.sample(lista, len(lista))
arbol = Arbol()

for i in lista:
    arbol.insertar(i)

print("Tamaño: " + str(tamaño) + " Pasos: " + str(arbol.insertar(10001)))