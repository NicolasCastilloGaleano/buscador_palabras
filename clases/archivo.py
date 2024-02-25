import os
import re

class Archivo:
    def __init__(self, ruta,palabra) -> None:
        self.nombre = os.path.basename(ruta)
        self.ruta = ruta
        self.palabra = palabra
        self.contenido = self.hallar_contenido()
        self.contador = self.contar_palabra()
        pass
    
    def hallar_contenido(self):
        with open(self.ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                return contenido
    
    def contar_palabra(self) -> int:
        contador = 0
        palabras = re.findall(r'\b\w+\b', self.contenido)
        for p in palabras:
            if p == self.palabra:
                contador += 1
        return contador