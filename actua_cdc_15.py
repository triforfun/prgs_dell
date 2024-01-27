import pandas as pd

# Rutas de los archivos
fich1_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/STOCKcdc.CSV'
fich2_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv'
log_file_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/error_log.txt'

try:
    print("Leyendo el fichero de entrada...")
    # Lee solo las dos primeras columnas (column1 y column2) del fichero de entrada con el carácter separador ";"
    df = pd.read_csv(fich1_path, usecols=range(26), sep=';', encoding='latin1', on_bad_lines='skip')

    print("Mostrando algunas líneas del fichero de entrada:")
    print(df.head())

    print("Renombrando columnas...")
    # Renombra las columnas de A a Z
    df.columns = [f'column{i}' for i in range(1, 27)]

    print("Seleccionando columnas A y B...")
    # Selecciona las columnas A (column1) y B (column2) del fichero de salida
    selected_columns = df[['column1', 'column2']]

    # Renombra las columnas
    selected_columns.columns = ['codigo_barras', 'stock_proveedor']

    print("Mostrando algunas líneas del fichero de salida:")
    print(selected_columns.head())

    print("Guardando en fichero de salida...")
    # Guarda el resultado en un nuevo fichero con las nuevas cabeceras en formato UTF-8
    selected_columns.to_csv(fich2_path, index=False, sep=';', encoding='utf-8')

except pd.errors.ParserError as e:
    print(f"Error al leer o procesar el archivo CSV: {e}")
    # Agrega la línea con error al archivo de registro (log)
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f"Error al leer o procesar el archivo CSV: {e}\n")

print("Proceso completado.")
