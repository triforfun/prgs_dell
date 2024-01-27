import os
import pandas as pd
fich1='c:/TFF/GESTIO/HIBOUTIK/CLIENTES/extract_clients.csv'
fich2='c:/TFF/GESTIO/HIBOUTIK/CLIENTES/ult_var.csv'

# Lee el fichero de entrada (fich1) con el carácter separador ";"
df = pd.read_csv(fich1, sep=';', encoding='utf-8')

# Selecciona las columnas 7 y 2
# selected_columns = df.iloc[:, [7, 2]]

# Renombra las columnas
# selected_columns.columns = ['codigo_barras', 'stock_proveedor']

# Guarda el resultado en un nuevo fichero (fich2 con las nuevas cabeceras en formato UTF-8
# selected_columns.to_csv(fich2, index=False, sep=';', encoding='utf-8')

ultima_act = df.iloc[0,22]

print ("ultima actualització: " , ultima_act)

print (df.iloc[:,22])

fichero = open(fich2, 'a')
fichero = open(fich2, 'w')
fichero.write(ultima_act)
fichero.close()





