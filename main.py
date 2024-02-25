from clases.carpeta import Carpeta

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

