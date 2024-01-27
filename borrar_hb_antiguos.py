import os
import shutil

# Ruta de la carpeta donde se encuentra el archivo
ruta_carpeta = 'c:/Users/onlin/Downloads'

# Nombre del archivo que se desea eliminar y mover
nombre_archivo1 = 'extract_produits.csv'
nombre_archivo2 = 'extract_produits_tailles.csv'

# Verificar si el archivo existe en la carpeta especificada
if os.path.exists(os.path.join(ruta_carpeta, nombre_archivo1)):
    # Eliminar el archivo
    os.remove(os.path.join(ruta_carpeta, nombre_archivo1))
    print(f'El archivo {nombre_archivo1} ha sido eliminado.')

else:
    print(f'El archivo {nombre_archivo1} no existe en la carpeta {ruta_carpeta}.')

if os.path.exists(os.path.join(ruta_carpeta, nombre_archivo2)):
    # Eliminar el archivo
    os.remove(os.path.join(ruta_carpeta, nombre_archivo2))
    print(f'El archivo {nombre_archivo2} ha sido eliminado.')

else:
    print(f'El archivo {nombre_archivo2} no existe en la carpeta {ruta_carpeta}.')

