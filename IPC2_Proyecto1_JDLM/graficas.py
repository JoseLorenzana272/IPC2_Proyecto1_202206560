import graphviz
from Lista_Enlazada import *

class Graph():
    def __init__(self, nombre):
        self.nombre = nombre
        self.dot = graphviz.Digraph(self.nombre, filename='structs.gv', node_attr={'shape': 'oval', 'fontname':'Helvetica'})

    #Tiempo y Amplitus de Señal
    def add(self, nodoInicio, nodoSiguiente, numero):
        self.dot.node(str(nodoInicio), str(nodoInicio))
        self.dot.node(str(nodoSiguiente), str(nodoSiguiente))
        self.dot.edge(str(nodoInicio), str(nodoSiguiente))

    #Valores de Frecuencia
    def add2(self, nodoInicio, nodoSiguiente, nombreInicio, nombreSiguiente):
        self.dot.node(str(nombreInicio), str(nodoInicio))
        self.dot.node(str(nombreSiguiente), str(nodoSiguiente))
        self.dot.edge(str(nombreInicio), str(nombreSiguiente))

    def generar(self, nombre):
        self.dot.render(filename=f'img/grafica_{nombre}', format='png').replace('\\', '/')
