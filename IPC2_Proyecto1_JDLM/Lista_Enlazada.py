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
            print(actual.dato.dato_frecuencia, actual.dato.dato_binario)
            
            actual = actual.siguiente

    def acceso(self):
        actual = self.cabeza
        while actual:
            actual.dato.datos.analisis(actual.dato.columna)
            actual = actual.siguiente
            global lista_comparación
            lista_comparación = ListaEnlazada()

    def analisis(self, valor):
        temporal = self.cabeza
        pos_y = temporal.dato.amplitud        
        contador = 0
        contador_prueba = 1
        print('\n')
        texto_binario = ''
        while contador != int(valor):
            if temporal is None:
                lista_comparación.agregar1(texto_binario)
                contador += 1
                contador_prueba += 1
                temporal = self.cabeza
                print(pos_y)
                pos_y = contador_prueba
                print('-'*50)
                texto_binario = ''
            else:
                if temporal.dato.amplitud == pos_y:
                    if contador == 0:
                        lista_comparación.agregar(str(temporal.dato.dato_binario))
                        print(temporal.dato.tiempo, pos_y, temporal.dato.dato_frecuencia, temporal.dato.dato_binario)
                    else:
                        texto_binario = texto_binario + str(temporal.dato.dato_binario)
                        print(temporal.dato.tiempo, pos_y, temporal.dato.dato_frecuencia, temporal.dato.dato_binario)
                temporal = temporal.siguiente
        lista_comparación.mostrar_temporal()

    def mostrar_temporal(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
    def agregar1(self, b):
        actual = self.cabeza
        for i in b:
            grupos = actual.dato
            actual.dato = grupos + i
            actual = actual.siguiente

                

lista_comparación = ListaEnlazada()

