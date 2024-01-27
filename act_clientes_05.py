# G:\Mi unidad\MiniPc\MpcSandbox
fich_cli1 ="G:/Mi unidad/MiniPc/MpcSandbox/extract_clients.csv"
nous_clients ="G:/Mi unidad/MiniPc/MpcSandbox/nous_clients.csv"
fich_ult ="G:/Mi unidad/MiniPc/MpcSandbox/ult_var.csv"
import pandas as pd

# Carga los datos
df = pd.read_csv(fich_cli1)
ult_act = pd.read_csv(fich_ult, header=None)

# Convierte las columnas a datetime
df['Ultima actualizacion'] = pd.to_datetime(df['Ultima actualizacion'])
ult_act[0] = pd.to_datetime(ult_act[0])

# Filtra las filas donde 'Ultima actualizacion' es posterior a la fecha en ult_act.csv
df_nuevos_clientes = df[df['Ultima actualizacion'] > ult_act.iloc[0,0]]

# Guarda el resultado en un nuevo archivo CSV
df_nuevos_clientes.to_csv(nous_clients, index=False)
