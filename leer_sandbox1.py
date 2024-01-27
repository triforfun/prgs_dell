import csv

with open('c:/TFF/SANDBOX/ot4_tots_sandbox.csv', encoding="utf8", newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=';', quotechar='"')
    for fila in lector_csv:
        print(fila)
