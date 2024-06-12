import random
import time as t
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

    def Long(self):
        cont = 0
        # nuevo_nodo = Nodo(item)
        if self.inicio is None:
            print("la lista esta vacia")
        else:
            puntero = self.inicio
            while puntero is not None:
                puntero = puntero.siguiente
                cont = cont + 1
        return cont


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

    def ordenamientoBurbuja(self):
        # nuevo_nodo = Nodo(dato)
        if self.inicio is None:
            print("la lista esta vacia")
        else:
            puntero = self.inicio
            while puntero is not None:
                puntero_siguente = puntero.siguiente
                while puntero_siguente is not None:
                    if puntero.dato > puntero_siguente.dato:
                        aux = puntero.dato
                        puntero.dato = puntero_siguente.dato
                        puntero_siguente.dato = aux
                    puntero_siguente = puntero_siguente.siguiente
                puntero = puntero.siguiente
                        # puntero.dato = puntero.siguiente.dato
                        # puntero1 = self.inicio
                        # self.inicio = nuevo_nodo  # El nuevo nodo se convierte en el primer nodo de la lista
                        # nuevo_nodo.siguiente = puntero
    # def ordenamiento_seleccion(self):
    #     if self.inicio is None:
    #         print("esta vacio")
    #     else:
    #         puntero = self.inicio
    #         while puntero is not None:
    #             puntero_siguente = puntero.siguiente
                
    #             while 
    def ordenamiento_seleccion(self):
        if self.inicio is None:
            print("La lista está vacía")
        else:
            puntero_actual = self.inicio
            while puntero_actual is not None:
                # Inicializar el nodo con el valor mínimo como el actual
                nodo_minimo = puntero_actual
                puntero_siguiente = puntero_actual.siguiente
                # Encontrar el nodo con el valor mínimo en el resto de la lista
                while puntero_siguiente is not None:
                    if puntero_siguiente.dato < nodo_minimo.dato:
                        nodo_minimo = puntero_siguiente
                    puntero_siguiente = puntero_siguiente.siguiente
                # Intercambiar los datos entre el nodo actual y el nodo mínimo encontrado
                puntero_actual.dato, nodo_minimo.dato = nodo_minimo.dato, puntero_actual.dato
                puntero_actual = puntero_actual.siguiente

a1 = Lista()



for i in range(1000):
    numero_entero = random.randint(0, 1000)
    a1.insertar_f(numero_entero)
a1.mostrar()
# print(numero_entero)
# # a1.insertar_i(20)
# a1.insertar_i(234)
# a1.insertar_i(1832)
# a1.insertar_i(1755)
# a1.insertar_i(1655)
# a1.mostrar()
tiempoa = t.time()
a1.ordenamiento_seleccion()
tiempob = t.time()
tiempoFnal = tiempob - tiempoa
tiempoInicial = t.time()
a1.ordenamientoBurbuja()
tiempoFinal = t.time()

total = tiempoFinal - tiempoInicial
print(total)
print(tiempoFnal)
# a1.mostrar()pr

# print(a1.Long())
a1.mostrar()