from clases.carpeta import Carpeta
# ruta 1 : archivos\pruebas1
# palabra 1 : arar
# ruta 2 : archivos\pruebas2
# palabra 2 : foto
# ruta 3 : archivos\Incorrecta
# palabra 3 : ejemplo

try:
    carpeta = input("Ingrese la ruta de la carpeta: ")
    palabra = input("Ingrese la palabra a buscar: ")

    prueba = Carpeta(carpeta, palabra)
    if len(prueba.archivos)>0:
        for archivo in prueba.archivos:
            print(archivo.nombre, ": ", archivo.contador, " veces")
        print("Total:       ", prueba.contador, " veces")
    else:
        print("no se encontraron archivos de texto en la carpeta")
except FileNotFoundError as e:
    print(e)

