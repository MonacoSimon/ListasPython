class Nodo:
     def __init__(self, dato):
          self.dato = dato
          self.derecha = None
          self.izquierda = None
class Arbol:
    def __init__(self):
          self.raiz = None

    def InsertarOrd(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz == None:
             self.raiz = nuevo_nodo
             return 
        else:
            aux = nuevo_nodo
            if aux > nuevo_nodo.izquierda.dato:
                 nuevo_nodo.izquierda = aux
            else:
                 self.derecha = aux
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


a1 = Arbol()
a1.InsertarOrd(3)
a1.InsertarOrd(2)
a1.InsertarOrd(1)
a1.imprimirOrd()
