import os
import pandas as pd

# Rutas de los archivos
fich1_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/STOCKcdc.CSV'
fich2_path = 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv'

# Verifica si el fichero de entrada existe
if not os.path.exists(fich1_path):
    print("NO EXISTE FICHERO DE ENTRADA")
else:
    # Verifica si el fichero actua_cdc2.csv existe y, en caso afirmativo, lo borra
    if os.path.exists(fich2_path):
        os.remove(fich2_path)

    # Lee el fichero de entrada con el carácter separador ";"
    df = pd.read_csv(fich1_path, sep=';', encoding='latin1')
   
    # Modifica los valores en la columna de índice 1 (stock_proveedor) si el valor en la columna de índice 0 es '>5'
    df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: 6 if x == '>5' else x)

    # Selecciona las columnas de índice 0 y 1
    selected_columns = df.iloc[:, [0, 1]]

    # Renombra las columnas
    selected_columns.columns = ['codigo_barras', 'stock_proveedor']

    # Guarda el resultado en un nuevo fichero con las nuevas cabeceras en formato UTF-8
    selected_columns.to_csv(fich2_path, index=False, sep=';', encoding='utf-8')
