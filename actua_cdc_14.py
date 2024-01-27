import os
import pandas as pd

# Rutas de los archivos
fich1_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/STOCKcdc.CSV'
fich2_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv'
log_file_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/error_log.txt'

# Verifica si el fichero de entrada existe
if not os.path.exists(fich1_path):
    print("NO EXISTE FICHERO DE ENTRADA")
else:
    try:
        print("Leyendo el fichero de entrada...")
        # Lee el fichero de entrada con el carácter separador ";"
        df = pd.read_csv(fich1_path, sep=';', encoding='latin1', on_bad_lines='skip')

        print("Mostrando algunas líneas del fichero de entrada:")
        print(df.head())

        print("Seleccionando columnas A y B...")
        # Selecciona las columnas A (EAN) y B (STOCK) del fichero de salida
        selected_columns = df[['EAN', 'STOCK']]

        # Renombra las columnas
        selected_columns.columns = ['codigo_barras', 'stock_proveedor']

        print("Mostrando algunas líneas del fichero de salida:")
        print(selected_columns.head())

        print("Guardando en fichero de salida...")
        # Guarda el resultado en un nuevo fichero con las nuevas cabeceras en formato UTF-8
        selected_columns.to_csv(fich2_path, index=False, sep=';', encoding='utf-8')
    
    except pd.errors.ParserError as e:
        print(f"Error al leer el archivo CSV: {e}")
        # Agrega la línea con error al archivo de registro (log)
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            if os.path.getsize(log_file_path) == 0:
                log_file.write("Errores al leer el archivo CSV:\n")
            log_file.write(f"{e}\n")

print("Proceso completado.")
