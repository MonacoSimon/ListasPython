class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, item):
        nuevo_nodo = Nodo(item)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            print("La pila está vacía, no se puede desapilar.")
            return None
        nodo_desapilado = self.cima
        self.cima = self.cima.siguiente
        return nodo_desapilado.dato

    def esta_vacia(self):
        return self.cima is None

    def ver_cima(self):
        if self.cima is None:
            print("La pila está vacía.")
            return None
        return self.cima.dato

    def mostrar(self):
        if self.cima is None:
            print("La pila está vacía.")
        else:
            actual = self.cima
            while actual is not None:
                print(actual.dato, end=" -> ")
                actual = actual.siguiente
            print("None")

# Crear una pila
mi_pila = Pila()

# Apilar elementos
mi_pila.apilar(10)
mi_pila.apilar(20)
mi_pila.apilar(30)

# Mostrar la pila
mi_pila.mostrar()  # Salida: 30 -> 20 -> 10 -> None

# Ver la cima
print("Cima:", mi_pila.ver_cima())  # Salida: Cima: 30

# Desapilar un elemento
print("Elemento desapilado:", mi_pila.desapilar())  # Salida: Elemento desapilado: 30

# Mostrar la pila después de desapilar
mi_pila.mostrar()  # Salida: 20 -> 10 -> None

# Verificar si la pila está vacía
print("¿Está vacía la pila?", mi_pila.esta_vacia())  # Salida: ¿Está vacía la pila? False

# Desapilar todos los elementos
mi_pila.desapilar()
mi_pila.desapilar()

# Intentar desapilar de una pila vacía
mi_pila.desapilar()  # Salida: La pila está vacía, no se puede desapilar.

# Mostrar la pila vacía
mi_pila.mostrar()  # Salida: La pila está vacía.