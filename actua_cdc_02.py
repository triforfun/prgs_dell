import os
import pandas as pd

fich1= 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/STOCKcdc.CSV'
fich2= 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv'


# Verifica si el fichero fich2.csv existe y, en caso afirmativo, lo borra
if os.path.exists(fich2):
    os.remove(fich2)

# Lee el fichero de entrada (fich1.csv) con el carácter separador ";"
df = pd.read_csv(fich1, sep=';', encoding='utf-8')

# Modifica los valores en la columna de índice 1 (stock_proveedor) si el valor en la columna de índice 0 es '>5'
df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: 6 if x == '>5' else x)

# Selecciona las columnas de índice 0 y 1
selected_columns = df.iloc[:, [0, 1]]

# Renombra las columnas
selected_columns.columns = ['codigo_barras', 'stock_proveedor']

# Guarda el resultado en un nuevo fichero (fich2.csv) con las nuevas cabeceras en formato UTF-8
selected_columns.to_csv('fich2.csv', index=False, sep=';', encoding='utf-8')