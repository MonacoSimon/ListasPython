class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class AB:
    def __init__(self):
        self.raiz = None

    def InsertarOrd(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            actual = self.raiz
            while True:
                # padre = actual
                dato1 = nuevo_nodo
                if dato1.dato < actual.dato:
                    actual = actual.izquierda
                    if actual is None:
                        padre.izquierda = nuevo_nodo
                        return
                else:
                    actual = actual.derecha
                    if actual is None:
                        padre.derecha = nuevo_nodo
                        return
                
    def imprimirOrd(self):
        actual = self.raiz
        pila = []
        while pila or actual:
            while actual:
                pila.append(actual)
                actual = actual.izquierda
            actual = pila.pop()
            print(actual.dato, " ")
            actual = actual.derecha

# Example usage
a1 = AB()
a1.InsertarOrd(3)
a1.InsertarOrd(2)
a1.InsertarOrd(1)

a1.imprimirOrd()

        



