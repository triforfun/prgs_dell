import pandas as pd

# Rutas de los archivos
fich1_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/STOCKcdc.CSV'
fich2_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv'
log_file_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/error_log.txt'

try:
    print("Leyendo el fichero de entrada...")
    # Lee solo las columnas A y B del fichero de entrada
    df = pd.read_csv(fich1_path, usecols=['EAN', 'STOCK'], sep=';', encoding='latin1', header=None)

    print("Renombrando columnas...")
    # Renombra las columnas
    df.columns = ['codigo_barras', 'stock_proveedor']

    print("Manejando columnas con múltiples URLs...")
    # Reemplaza las celdas con múltiples URLs en la columna URL_IMAGEN
    df['URL_IMAGEN'] = df.apply(lambda row: row[0].split(';')[9] if len(row[0].split(';')) > 9 else '', axis=1)

    print("Mostrando algunas líneas del fichero de salida:")
    print(df.head())

    print("Guardando en fichero de salida...")
    # Guarda el resultado en un nuevo fichero con las nuevas cabeceras en formato UTF-8
    df.to_csv(fich2_path, index=False, sep=';', encoding='utf-8')

except pd.errors.ParserError as e:
    print(f"Error al leer o procesar el archivo CSV: {e}")
    # Agrega la línea con error al archivo de registro (log)
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f"Error al leer o procesar el archivo CSV: {e}\n")

print("Proceso completado.")
