import os
import pandas as pd

fich1= 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/STOCKcdc.csv'
fich2= 'C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/actua_cdc2.csv'


# Verifica si el fichero fich2.csv existe y, en caso afirmativo, lo borra
if os.path.exists(fich2):
    os.remove(fich2)

# Lee el fichero de entrada (fich1.csv) con el carácter separador ";"

df = pd.read_csv(fich1, sep=';', encoding='latin1')

# Selecciona las columnas 5 y 6
selected_columns = df.iloc[:, [0, 1]]

# Renombra las columnas
selected_columns.columns = ['codigo_barras', 'stock_proveedor']

# Guarda el resultado en un nuevo fichero (fich2 con las nuevas cabeceras en formato UTF-8
selected_columns.to_csv(fich2, index=False, sep=';', encoding='utf-8')
