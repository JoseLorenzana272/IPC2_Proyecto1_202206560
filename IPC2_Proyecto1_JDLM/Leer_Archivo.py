import xml.etree.ElementTree as ET
from Lista_Enlazada import ListaEnlazada
from Frecuencias import Frecuencia
from Señales import señales

#Crear Lista Enlazada
lista_señales = ListaEnlazada()
lista_señal_datos = ListaEnlazada()

class Leer_Archivo_xml:
    def leer_xml(self, ruta_archivo):
        # Cargar el archivo XML
        tree = ET.parse('entrada.xml')
        root = tree.getroot()
        global lista_señal_datos
        # Iterar a través de las señales y sus datos
        for senal in root.findall('senal'):
            nombre = senal.get('nombre')
            fila = senal.get('t')
            columna = senal.get('A')
            

            for dato in senal.findall('dato'):
                t = dato.get('t')
                a = dato.get('A')
                valor = dato.text
                
                datos_f = Frecuencia(t, a, valor)
                lista_señal_datos.agregar(datos_f)
        
            datos_s = señales(nombre, fila, columna, lista_señal_datos)
            lista_señales.agregar(datos_s)
            lista_señal_datos = ListaEnlazada()




