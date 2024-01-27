fich_cli1 ="G:/Mi unidad/MiniPc/MpcSandbox/extract_clients.csv"
nous_clients ="G:/Mi unidad/MiniPc/MpcSandbox/nous_clients.csv"
fich_ult ="G:/Mi unidad/MiniPc/MpcSandbox/ult_act.csv"

import pandas as pd

# Carga los datos
df = pd.read_csv(fich_cli1, sep=';', encoding='utf-8', on_bad_lines='warn')
ult_act = pd.read_csv(fich_ult, header=None)

# Convierte las columnas a datetime
df['Ultima actualización'] = pd.to_datetime(df['Ultima actualización'])
ult_act[0] = pd.to_datetime(ult_act[0])

# Filtra las filas donde 'Ultima actualización' es posterior a la fecha en ult_act.csv
df_nuevos_clientes = df[df['Ultima actualización'] > ult_act.iloc[0,0]]

# Guarda el resultado en un nuevo archivo CSV con codificación UTF-8 y separador ';'
df_nuevos_clientes.to_csv(nous_clients, sep=';', encoding='utf-8', index=False)

# Encuentra el valor más reciente de 'Ultima actualización'
ultima_actualizacion_mas_reciente = df['Ultima actualización'].max()

# Crea un nuevo DataFrame y guárdalo en ult_act.csv
pd.DataFrame([ultima_actualizacion_mas_reciente]).to_csv(fich_ult, header=False, index=False)
