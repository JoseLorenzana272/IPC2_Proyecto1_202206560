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
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        global lista_señal_datos
        # Iterar a través de las señales y sus datos
        for senal in root.findall('senal'):
            nombre = senal.get('nombre')
            fila = senal.get('t')
            columna = senal.get('A')
            #contador_t = 0

            for dato in senal.findall('dato'):
                t = dato.get('t')
                a = dato.get('A')
                if int(t) > 0 and int(t) <= 3600 and int(a) > 0 and int(a) <= 130:  # Corregir la condición aquí
                    valor = dato.text
                    if t <= fila and a <= columna:
                        if int(valor) == 0:
                            datos_f = Frecuencia(int(t), int(a), valor, 0, 0, 0, '')
                            lista_señal_datos.agregar(datos_f)
                        else: 
                            datos_f = Frecuencia(int(t), int(a), valor, 1, 0, 0, '')
                            lista_señal_datos.agregar(datos_f)
                #contador_t += 1

            datos_s = señales(nombre, fila, columna, lista_señal_datos)
            lista_señales.agregar(datos_s)
            lista_señal_datos = ListaEnlazada()




