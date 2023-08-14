from Nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato.nombre)
            actual.dato.datos.mostrar1()
            actual = actual.siguiente

    def mostrar1(self):
        actual = self.cabeza
        while actual:
            print(actual.dato.tiempo, actual.dato.amplitud, actual.dato.dato_frecuencia)
            actual = actual.siguiente
        

