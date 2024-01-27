import os
import shutil

# Ruta de la carpeta donde se encuentra el archivo
ruta_carpeta = '/ruta/a/la/carpeta'

# Nombre del archivo que se desea eliminar y mover
nombre_archivo = 'archivo.txt'

# Verificar si el archivo existe en la carpeta especificada
if os.path.exists(os.path.join(ruta_carpeta, nombre_archivo)):
    # Eliminar el archivo
    os.remove(os.path.join(ruta_carpeta, nombre_archivo))
    print(f'El archivo {nombre_archivo} ha sido eliminado.')

    # Ruta de la carpeta a donde se desea mover el archivo
    ruta_carpeta_destino = '/ruta/a/la/carpeta/de/destino'

    # Mover el archivo a la carpeta de destino
    shutil.move(os.path.join(ruta_carpeta, nombre_archivo), ruta_carpeta_destino)
    print(f'El archivo {nombre_archivo} ha sido movido a la carpeta {ruta_carpeta_destino}.')
else:
    print(f'El archivo {nombre_archivo} no existe en la carpeta {ruta_carpeta}.')
