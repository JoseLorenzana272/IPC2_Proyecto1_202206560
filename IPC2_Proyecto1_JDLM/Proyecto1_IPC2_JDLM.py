from colorama import Fore, init
from Leer_Archivo import *
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os
from Lista_Enlazada import *

def mostrar_menu():
    while True:
        print(f"{Fore.LIGHTWHITE_EX}-------------Menú:-------------")
        print(f"{Fore.YELLOW}1. Cargar Archivo")
        print(f"{Fore.YELLOW}2. Procesar Archivo")
        print(f"{Fore.YELLOW}3. Escribir Archivo Salida")
        print(f"{Fore.YELLOW}5. Mostrar Datos del Estudiante")
        print(f"{Fore.YELLOW}6. Generar Gráfica")
        print(f"{Fore.YELLOW}7. Salir")
        
        opcion = input(f"{Fore.LIGHTWHITE_EX}Seleccione una opción (1-4): ")
        
        if opcion == "1":
            # Cargar Archivo
            os.system("cls")
            ruta = input(f"{Fore.LIGHTWHITE_EX}Ingrese la ruta del archivo: ")
            print(f"{Fore.GREEN}Ha seleccionado la opción 1; Cargar Inventario Inicial")
            Leer_Archivo_xml().leer_xml(ruta)
            lista_señales.mostrar()

        elif opcion == "2":
            # Procesar Archivo
            os.system("cls")
            print(f"{Fore.GREEN}Ha seleccionado la opción 2; Procesar Archivo")
            print(f'{Fore.LIGHTMAGENTA_EX}Calculando la matriz binaria...')
            print(f'{Fore.LIGHTMAGENTA_EX}Calculando...')
            lista_señales.acceso()
        elif opcion == "3":
            # Escribir Archivo Salida
            os.system("cls")
            print(f"{Fore.GREEN}Ha seleccionado la opción 3.")
            print('Archivo generado exitosamente...')
            root = ET.Element("senalesReducidas")
            lista_grupos.escribir_xml(root)
            xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
            # Guardar el XML formateado en un archivo
            with open("final.xml", "w") as f:
                f.write(xmlstr)
        elif opcion == "4":
            # Crear Informe de Movimientos
            os.system("cls")
            print(f"{Fore.GREEN}Ha seleccionado la opción 4.")
        elif opcion == "5":
            # Mostrar Datos del Estudiantes
            os.system("cls")
            print(f"{Fore.GREEN}Ha seleccionado la opción 5.")
            print(f'Nombre: José Daniel Lorenzana Medina\nCarné: 202206560\nCurso: Introducción a la Programación y Computación 2\nSección: "A"\nCarrera: Ingeniería en Ciencias y Sistemas\nSemestre: 4to Semestre')
        elif opcion == "6":
            # Generar Gráfica
            os.system("cls")
            print(f"{Fore.GREEN}Ha seleccionado la opción 6.")
        
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-4).")

mostrar_menu()