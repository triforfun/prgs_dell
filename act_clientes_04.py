import csv
from datetime import datetime

def comparar_fechas(fecha_cliente, fecha_referencia):
    formato_fecha = "%d/%m/%Y %H:%M:%S"
    try:
        fecha_cliente = datetime.strptime(fecha_cliente, formato_fecha)
        fecha_referencia = datetime.strptime(fecha_referencia, formato_fecha)
        return fecha_cliente > fecha_referencia  # Cambiado de >= a >
    except ValueError as e:
        print(f"Error al convertir fechas: {e}")
        return False

def copiar_lineas_superiores(fichero_entrada, fecha_referencia, fichero_salida):
    with open(fichero_entrada, 'r', newline='', encoding='utf-8') as csv_entrada:
        lector = csv.reader(csv_entrada)
        encabezado = next(lector)  # Leer encabezado

        indice_fecha_ult_act = 22  # Índice de la columna con la fecha de última actualización

        with open(fichero_salida, 'w', newline='', encoding='utf-8') as csv_salida:
            escritor = csv.writer(csv_salida)
            escritor.writerow(encabezado)  # Escribir encabezado en el nuevo archivo

            for i, linea in enumerate(lector, start=2):  # Empezar desde la segunda línea
                # Verificar si la línea tiene el número correcto de elementos
                if len(linea) > indice_fecha_ult_act:
                    fecha_ult_act_cliente = linea[indice_fecha_ult_act]

                    # Asegurarse de que la fecha esté en el formato correcto antes de comparar
                    if "/" in fecha_ult_act_cliente:
                        if comparar_fechas(fecha_ult_act_cliente, fecha_referencia):
                            escritor.writerow(linea)
                    else:
                        print(f"Advertencia: La línea {i} en {fichero_entrada} tiene un formato de fecha incorrecto y será ignorada.")
                else:
                    print(f"Advertencia: La línea {i} en {fichero_entrada} no tiene el número correcto de elementos y será ignorada.")

# Nombres y ubicaciones de los archivos
fich1 = 'c:/TFF/GESTIO/HIBOUTIK/CLIENTES/extract_clients.csv'
fich2 = 'c:/TFF/GESTIO/HIBOUTIK/CLIENTES/ult_var.csv'
fich3 = 'c:/TFF/GESTIO/HIBOUTIK/CLIENTES/act_clientes.csv'

clientes_csv = fich1
ult_var_csv = fich2
act_clientes_csv = fich3

# Leer la fecha de referencia desde el archivo ult_var.csv
with open(ult_var_csv, 'r', newline='', encoding='utf-8') as csv_var:
    lector_var = csv.reader(csv_var)
    fecha_referencia = next(lector_var)[0]

# Formatear la fecha de referencia al mismo formato que en extract_clients.csv
fecha_referencia = datetime.strptime(fecha_referencia, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")

print(f"Fecha de referencia: {fecha_referencia}")

# Copiar las líneas que cumplen con la condición en el nuevo archivo
copiar_lineas_superiores(clientes_csv, fecha_referencia, act_clientes_csv)

print(f"Proceso completado. Las líneas se han copiado en {act_clientes_csv}.")
