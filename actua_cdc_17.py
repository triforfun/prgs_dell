import csv
import pandas as pd
# Rutas de los archivos
fich1_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/STOCKcdc.CSV'
fich2_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv'
log_file_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/error_log.txt'

try:
    print("Leyendo el fichero de entrada...")
    with open(fich1_path, 'r', encoding='latin1') as file:
        csv_reader = csv.reader(file, delimiter=';')
        
        # Leer las cabeceras
        headers = next(csv_reader)
        # Seleccionar índices de las columnas de interés
        indices = [headers.index('EAN'), headers.index('STOCK')]

        # Lista para almacenar las filas procesadas
        processed_rows = []

        # Procesar el resto del archivo
        for row in csv_reader:
            # Filtrar las columnas de interés
            selected_columns = [row[i] if i < len(row) else '' for i in indices]
            # Unir las columnas seleccionadas
            processed_rows.append(selected_columns)

    # Crear un DataFrame con los resultados
    df = pd.DataFrame(processed_rows, columns=['codigo_barras', 'stock_proveedor'])

    print("Mostrando algunas líneas del fichero de salida:")
    print(df.head())

    print("Guardando en fichero de salida...")
    # Guarda el resultado en un nuevo fichero con las nuevas cabeceras en formato UTF-8
    df.to_csv(fich2_path, index=False, sep=';', encoding='utf-8')

except Exception as e:
    print(f"Error al leer o procesar el archivo CSV: {e}")
    # Agrega la línea con error al archivo de registro (log)
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f"Error al leer o procesar el archivo CSV: {e}\n")

print("Proceso completado.")
