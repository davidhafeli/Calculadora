from tkinter import *

from Resultados_Pantalla import *


def pulsaciones_teclas(self, valor, mostrar):
        
        if mostrar:
            
            self.operacion+=str(valor)
            
            mostrar_pantalla(self,valor) # pasarle por parametro el self a la funcion mostrar pantalla
            
        elif not mostrar and valor=="=":
            
            borrar_pantalla(self)
            
            mostrar_pantalla(self, str(eval(self.operacion)))
            
        else:
            
            pass