import xml.etree.ElementTree as ET
from Lista_Enlazada import ListaEnlazada
from Frecuencias import Frecuencia
from Señales import señales
from colorama import Fore

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
            contador_t = 1
            if int(fila) > 0 and int(fila) <= 3600 and int(columna) > 0 and int(columna) <= 130:  # Corregir la condición aquí
                for dato in senal.findall('dato'):
                    t = dato.get('t')
                    a = dato.get('A')
                    if int(t) <= int(fila) and int(a) <= int(columna):
                        valor = dato.text
                        #contador_temp += 1
                        if valor is None:
                            print(f'{Fore.RED}Error, en la señal {nombre} en el dato {t},  {a} no tiene valor')
                            datos_f = Frecuencia(int(t), int(a), '0', 0, 0, 0, '', nombre+'_'+str(contador_t))
                            contador_t += 1
                            lista_señal_datos.agregar(datos_f)
                        else:
                            
                            if int(valor) == 0:
                                datos_f = Frecuencia(int(t), int(a), valor, 0, 0, 0, '', nombre+'_'+str(contador_t))
                                contador_t += 1
                                lista_señal_datos.agregar(datos_f)
                            else: 
                                datos_f = Frecuencia(int(t), int(a), valor, 1, 0, 0, '', nombre+'_'+str(contador_t))
                                contador_t += 1
                                lista_señal_datos.agregar(datos_f)
                
            lista_señal_datos.ordenar_por_t_a()
            datos_s = señales(nombre, fila, columna, lista_señal_datos)
            lista_señales.agregar(datos_s)
            lista_señal_datos = ListaEnlazada()




