import os
import shutil

if os.path.exists("c:/maq_dell.txt"):
    print("existe maq_dell.txt")

ruta_carpeta = 'c:/Users/onlin/Downloads'
ruta_carpeta_destino = 'c:/TFF/DOCS/ONLINE/STOCKS_EXTERNS'
ruta_carpeta_destino_ORCA = 'c:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/ORCA'
# Nombre del archivo que se desea eliminar y mover
nombre_archivo1 = 'extract_produits.csv'
nombre_archivo2 = 'extract_produits_tailles.csv'
nombre_archivo3 = 'informe-maesarti.csv'

nombre_archivo4Down = 'list.csv'
nombre_archivo4Stock = "STOCK_ORCA.csv"

# Verificar si el archivo existe en la carpeta especificada
if os.path.exists(os.path.join(ruta_carpeta_destino, nombre_archivo1)):
    # Eliminar el archivo de destino
    os.remove(os.path.join(ruta_carpeta_destino, nombre_archivo1))
    print(f'El archivo {nombre_archivo1} ha sido eliminado.')
  
    # Mover el archivo a la carpeta de destino
    shutil.move(os.path.join(ruta_carpeta, nombre_archivo1), ruta_carpeta_destino)
    print(f'El archivo {nombre_archivo1} ha sido movido a la carpeta {ruta_carpeta_destino}.')
else:
    print(f'El archivo {nombre_archivo1} no existia en la carpeta {ruta_carpeta_destino}.')

# Verificar si el archivo2 existe en la carpeta especificada
if os.path.exists(os.path.join(ruta_carpeta_destino, nombre_archivo2)):
    # Eliminar el archivo
    os.remove(os.path.join(ruta_carpeta_destino, nombre_archivo2))
    print(f'El archivo {nombre_archivo2} ha sido eliminado.')
    # Mover el archivo a la carpeta de destino
    shutil.move(os.path.join(ruta_carpeta, nombre_archivo2), ruta_carpeta_destino)
    print(f'El archivo {nombre_archivo2} ha sido movido a la carpeta {ruta_carpeta_destino}.')
else:
    print(f'El archivo {nombre_archivo2} no existía en la carpeta {ruta_carpeta_destino}.')

# Verificar si el archivo3 existe en la carpeta especificada
if os.path.exists(os.path.join(ruta_carpeta_destino, nombre_archivo3)):
    # Eliminar el archivo
    os.remove(os.path.join(ruta_carpeta_destino, nombre_archivo3))
    print(f'El archivo {nombre_archivo3} ha sido eliminado.')
    # Mover el archivo a la carpeta de destino
    shutil.move(os.path.join(ruta_carpeta, nombre_archivo3), ruta_carpeta_destino)
    print(f'El archivo {nombre_archivo3} ha sido movido a la carpeta {ruta_carpeta_destino}.')
else:
    print(f'El archivo {nombre_archivo3} no existía en la carpeta {ruta_carpeta_destino}.')

 # Verificar si el archivo4 existe en la carpeta especificada
if os.path.exists(os.path.join(ruta_carpeta_destinoORCA, nombre_archivo4Stock)):
    # Eliminar el archivo
    os.remove(os.path.join(ruta_carpeta_destino, nombre_archivo4Stock))
    print(f'El archivo {nombre_archivo4Stock} ha sido eliminado.')
    # Mover el archivo a la carpeta de destino
    shutil.move(os.path.join(ruta_carpeta, nombre_archivo4Down), ruta_carpeta_destino)
    os.rename("c:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/ORCA/list.csv","c:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/ORCA/STOCK_ORCA.CSV")
    print(f'El archivo {nombre_archivo4Down} ha sido movido a la carpeta {ruta_carpeta_destino}.')
    
else:
    print(f'El archivo {nombre_archivo4Stock} no existía en la carpeta {ruta_carpeta_destino}.')
