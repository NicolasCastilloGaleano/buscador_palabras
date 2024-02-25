from .archivo import Archivo
import glob
import os

class Carpeta:
    def __init__(self, ruta, palabra) -> None:
        if os.path.exists(ruta) and os.path.isdir(ruta):
            self.ruta = ruta
            self.palabra = palabra
            self.contador=0
            self.archivos : list[Archivo] = []
            self.buscar_archivos()
            self.contar_palabra()
        else:
            raise FileNotFoundError("no se encuentra la carpeta indicada")

    def buscar_archivos(self) -> None:
        rutas = glob.glob(self.ruta + '/*.txt') + glob.glob(self.ruta + '/*.xml') + glob.glob(self.ruta + '/*.json') + glob.glob(self.ruta + '/*.csv')
        for ruta in rutas:
            self.archivos.append(Archivo(ruta,self.palabra))
            
    def contar_palabra(self) -> None:
        for archivo in self.archivos:
            self.contador+= archivo.contador