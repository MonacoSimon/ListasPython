class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Inicializamos el puntero al siguiente nodo como None

class Lista:
    def __init__(self):
        self.inicio = None  # Inicializamos el inicio de la lista como None, indicando que la lista está vacía

    def insertar_f(self, item):
        aux = Nodo(item)  # Creamos un nuevo nodo con el valor 'item'
        if self.inicio is None:  # Si la lista está vacía
            self.inicio = aux  # El nuevo nodo se convierte en el primer nodo de la lista
        else:
            puntero = self.inicio
            while puntero.siguiente is not None:  # Recorremos la lista hasta el último nodo
                puntero = puntero.siguiente
            puntero.siguiente = aux  # Enlazamos el nuevo nodo al último nodo de la lista

    def insertar_i(self, item):
        aux = Nodo(item)  # Creamos un nuevo nodo con el valor 'item'
        if self.inicio is None:  # Si la lista está vacía
            self.inicio = aux  # El nuevo nodo se convierte en el primer nodo de la lista
        else:
            puntero = self.inicio
            self.inicio = aux  # El nuevo nodo se convierte en el primer nodo de la lista
            aux.siguiente = puntero  # Enlazamos el antiguo primer nodo al nuevo primer nodo

    def eliminar_i(self):
        if self.inicio is None:  # Si la lista está vacía
            print("Lista vacía, no se puede eliminar elemento")
        else:
            self.inicio = self.inicio.siguiente  # El segundo nodo se convierte en el primero, eliminando el primero

    def eliminar_f(self):
        if self.inicio is None:  # Si la lista está vacía
            print("Lista vacía, no se puede eliminar elemento")
        else:
            punteroant = self.inicio
            punteropost = self.inicio

            while punteropost.siguiente is not None:  # Recorremos la lista hasta el penúltimo nodo
                punteroant = punteropost
                punteropost = punteropost.siguiente

            if punteroant == punteropost:  # Si solo hay un elemento en la lista
                self.inicio = None  # La lista queda vacía
            else:
                punteroant.siguiente = None  # El penúltimo nodo deja de apuntar al último nodo, eliminándolo

    def insertar_p(self, item, pos):
        aux = Nodo(item)  # Creamos un nuevo nodo con el valor 'item'
        if self.inicio is None:  # Si la lista está vacía
            print("La lista está vacía")
        else:
            puntero = self.inicio
            if pos == 1:  # Si la posición es 1
                self.inicio = aux  # El nuevo nodo se convierte en el primer nodo de la lista
                aux.siguiente = puntero  # Enlazamos el antiguo primer nodo al nuevo primer nodo
            else:
                for _ in range(1, pos - 1):  # Recorremos la lista hasta la posición deseada
                    puntero = puntero.siguiente
                    if puntero.siguiente is None:
                        break
                punteronext = puntero.siguiente
                puntero.siguiente = aux  # Insertamos el nuevo nodo en la posición deseada
                aux.siguiente = punteronext

    def mostrar(self):
        if self.inicio is None:  # Si la lista está vacía
            print("La lista está vacía")
        else:
            puntero = self.inicio
            print(f"{puntero.dato} ->", end=" \t")  # Mostramos el primer nodo de la lista
            while puntero.siguiente is not None:  # Recorremos la lista hasta el último nodo
                puntero = puntero.siguiente
                print(f"{puntero.dato} ->", end=" \t")  # Mostramos cada nodo de la lista
        print()  # Imprimimos una línea en blanco al final para separar la salida


a1 = Lista()

a1.insertar_i(20)
a1.mostrar()