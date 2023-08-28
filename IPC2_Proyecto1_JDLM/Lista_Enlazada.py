from Nodo import Nodo
from grupos import Grupos
from sumatorias import Sumar
from grupos_analizados import analisis_grupo
from colorama import Fore, init
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
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
            print(f'T: {actual.dato.tiempo}', f'A: {actual.dato.amplitud}', f'Comparado: {actual.dato.valor_comparado}', f'Ya Comparado: {actual.dato.ya_comparado}')
            
            actual = actual.siguiente

    def acceso(self):
        actual = self.cabeza
        while actual:
            global lista_comparación
            global lista_sumas
            actual.dato.datos.analisis(actual.dato.columna, actual.dato.fila)
            lista_comparación.lectura_comparado(actual.dato.fila, actual.dato.datos)
            #print(f'SEÑAL: {actual.dato.nombre}\n')
            actual.dato.datos.sumar(actual.dato.fila, actual.dato.columna)
            guardar_grupos = analisis_grupo(actual.dato.nombre, lista_sumas, actual.dato.columna)
            lista_grupos.agregar(guardar_grupos)
            #print(f'\n\n\n')
            actual = actual.siguiente
            lista_comparación = ListaEnlazada()
            lista_sumas = ListaEnlazada()
        lista_grupos.mostrar_grupos()
            

    def analisis(self, valor, fila_t):
        temporal = self.cabeza
        pos_y = temporal.dato.amplitud        
        contador = 0
        contador_prueba = 1 
        texto_binario = ''
        while contador != int(valor):
            if temporal is None:
                lista_comparación.agregar1(texto_binario)
                contador += 1
                contador_prueba += 1
                temporal = self.cabeza
                pos_y = contador_prueba
                texto_binario = ''
            else:
                if temporal.dato.amplitud == pos_y:
                    if contador == 0:
                        dato_agregado = Grupos(str(temporal.dato.dato_binario), 0)
                        lista_comparación.agregar(dato_agregado)
                        
                    else:
                        texto_binario = texto_binario + str(temporal.dato.dato_binario)
                        
                temporal = temporal.siguiente
        
        lista_comparación.comparar(fila_t)

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

    
    def lectura_comparado(self, fila_tiempo, datos_cambiados):
        actual = self.cabeza
        for i in range(1, int(fila_tiempo)+1):
            datos_cambiados.asignar_comparado(actual.dato.verificador, i, actual.dato.dato_binario)
            actual = actual.siguiente

    def asignar_comparado(self, comparacion_dato, fila_tiempo, dato_binario):
        actual = self.cabeza
        while actual:
            if actual.dato.tiempo == fila_tiempo:
                actual.dato.valor_comparado  = comparacion_dato
                actual.dato.linea_r = dato_binario
            actual = actual.siguiente
                
    def lectura_suma(self, fila, datos):
        actual = self.cabeza
        for i in range(1, int(fila)+1):
            datos.sumar(i, fila)
            actual = actual.siguiente

    def sumar(self, valor, limite):
        limite_nuevo = (int(limite)*int(valor))
        valor_nuevo = int(limite)
        actual = self.cabeza
        grupo_suma = ''
        nombre_grupo = ''
        terminal = 0
        sumatoria = 0
        nuevo_contador = 1
        contador2 = 0
        contador_grupo = 0
        y = actual.dato.amplitud
        while terminal != limite_nuevo:
            if actual is None:
                actual = self.cabeza
                y += 1
                if contador2 > 0:
                    if grupo_suma != '':
                        grupo_suma = grupo_suma + str(sumatoria)
                    else:
                        grupo_suma = str(sumatoria)
                    contador2 = 0
                sumatoria = 0
                terminal += 1
                if y == valor_nuevo+1:
                    y = 1
                    if grupo_suma != '':
                        contador_grupo += 1
                        dato_agregado = Sumar(contador_grupo, nombre_grupo, grupo_suma)
                        lista_sumas.agregar(dato_agregado)
                    nombre_grupo = ''
                    grupo_suma = ''
                    nuevo_contador += 1
                
            else:
                if actual.dato.amplitud == y and actual.dato.valor_comparado == nuevo_contador and actual.dato.ya_comparado == 0:
                    contador2 += 1
                    sumatoria += int(actual.dato.dato_frecuencia)
                    actual.dato.ya_comparado = 1
                    if nombre_grupo == '':
                        nombre_grupo = str(actual.dato.tiempo)
                        
                    else:
                    
                        if str(actual.dato.tiempo) not in nombre_grupo:
                            nombre_grupo = nombre_grupo + ',' + str(actual.dato.tiempo)
            actual = actual.siguiente

    

    def mostrar_grupos(self):
        actual = self.cabeza
        while actual:
            print(f'{Fore.LIGHTCYAN_EX}{actual.dato.nombre_grupo}')
            actual.dato.lista_grupos.mostrar_sumas()
            actual = actual.siguiente

    def mostrar_sumas(self):
        actual = self.cabeza
        while actual:
            print(f'{Fore.LIGHTWHITE_EX}', actual.dato.numero_grupo, actual.dato.grupo, actual.dato.sumatorias)
            actual = actual.siguiente
                

    def escribir_xml(self, referencia):
        actual = self.cabeza
        while actual:
            señal_nombre = ET.SubElement(referencia, "senal", nombre=actual.dato.nombre_grupo, A=actual.dato.amplitud_salida)
            actual.dato.lista_grupos.salida(señal_nombre)
            
            actual = actual.siguiente

    def salida(self, referencia):
        actual = self.cabeza
        while actual:
            grupo_nombre = ET.SubElement(referencia, "grupo", g=str(actual.dato.numero_grupo))
            tiempos = ET.SubElement(grupo_nombre, "tiempos")
            tiempos.text = actual.dato.grupo
            datos_grupo = ET.SubElement(grupo_nombre, "datosGrupo")
            contador_amplitud = 0
            for i in actual.dato.sumatorias:
                contador_amplitud += 1
                dato = ET.SubElement(datos_grupo, "dato", A=str(contador_amplitud))
                dato.text = str(i)
            actual = actual.siguiente

lista_comparación = ListaEnlazada()
lista_sumas = ListaEnlazada()
lista_grupos = ListaEnlazada()