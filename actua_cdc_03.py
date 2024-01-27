import os
import pandas as pd

# Verifica si el fichero actua_cdc2.csv existe y, en caso afirmativo, lo borra
if os.path.exists('C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv'):
    os.remove('C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv')

# Lee el fichero de entrada (STOCKcdc.CSV) con el carácter separador ";"
df = pd.read_csv('C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/STOCKcdc.CSV', sep=';', encoding='utf-8')

# Modifica los valores en la columna de índice 1 (stock_proveedor) si el valor en la columna de índice 0 es '>5'
df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: 6 if x == '>5' else x)

# Selecciona las columnas de índice 0 y 1
selected_columns = df.iloc[:, [0, 1]]

# Renombra las columnas
selected_columns.columns = ['codigo_barras', 'stock_proveedor']

# Guarda el resultado en un nuevo fichero (actua_cdc2.csv) con las nuevas cabeceras en formato UTF-8
selected_columns.to_csv('C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv', index=False, sep=';', encoding='utf-8')
