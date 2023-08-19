from Nodo import Nodo
from grupos import Grupos

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
            print(f'Tiempo Máximo: {actual.dato.fila}')
            actual.dato.datos.mostrar1()
            actual = actual.siguiente

    def mostrar1(self):
        actual = self.cabeza
        while actual:
            print(f'Dato de Señal: {actual.dato.dato_frecuencia}', f'Dato Binario: {actual.dato.dato_binario}')
            actual = actual.siguiente

    def acceso(self):
        actual = self.cabeza
        while actual:
            actual.dato.datos.analisis(actual.dato.columna, actual.dato.fila)
            actual = actual.siguiente
            global lista_comparación
            lista_comparación = ListaEnlazada()

    def analisis(self, valor, fila_t):
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
                        dato_agregado = Grupos(str(temporal.dato.dato_binario), 0)
                        lista_comparación.agregar(dato_agregado)
                        print(temporal.dato.tiempo, pos_y, temporal.dato.dato_frecuencia, temporal.dato.dato_binario)
                        
                    else:
                        texto_binario = texto_binario + str(temporal.dato.dato_binario)
                        print(temporal.dato.tiempo, pos_y, temporal.dato.dato_frecuencia, temporal.dato.dato_binario)
                temporal = temporal.siguiente
        lista_comparación.mostrar_temporal()
        lista_comparación.comparar(fila_t)
        lista_comparación.mostrar_temporal()

    def mostrar_temporal(self):
        actual = self.cabeza
        while actual:
            print(actual.dato.dato_binario, actual.dato.verificador)
            actual = actual.siguiente
    
    def agregar1(self, b):
        actual = self.cabeza
        for i in b:
            grupos = actual.dato.dato_binario
            actual.dato.dato_binario = grupos + i
            actual = actual.siguiente

    def comparar(self, fila_tiempo):
        actual = self.cabeza
        for i in range(1, int(fila_tiempo)+1):
            lista_comparación.comparar2(actual.dato.dato_binario, i)
            actual = actual.siguiente

    def comparar2(self, dato, posicion):
        temporal = self.cabeza
        while temporal:
                
                if dato == temporal.dato.dato_binario:
                    
                    if temporal.dato.verificador == 0:
                        temporal.dato.verificador = posicion
                        
                temporal = temporal.siguiente

    

                

lista_comparación = ListaEnlazada()

