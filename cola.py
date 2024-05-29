class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, item):
        nuevo_nodo = Nodo(item)
        if self.final is None:  # Si la cola está vacía
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        if self.frente is None:  # Si la cola está vacía
            print("La cola está vacía, no se puede desencolar.")
            return None
        else:
            dato_desencolado = self.frente.dato
            self.frente = self.frente.siguiente
            if self.frente is None:  # Si la cola estaba compuesta por un solo elemento
                self.final = None
            return dato_desencolado

    def esta_vacia(self):
        return self.frente is None

    def ver_frente(self):
        if self.frente is None:
            print("La cola está vacía.")
            return None
        else:
            return self.frente.dato

    def mostrar(self):
        if self.frente is None:
            print("La cola está vacía.")
        else:
            actual = self.frente
            while actual is not None:
                print(actual.dato, end=" -> ")
                actual = actual.siguiente
            print("None")