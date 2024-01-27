import os
import shutil
from os import remove
from pathlib import Path

ficherolog="C:/py_rafa/descarregues.log"
destino1="C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS"
destinohoka="C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/HOKA"
destinoArena="C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/ARENA"

fichdestino1Hoka = destinohoka+"/HOKAFEETURES FW23 Especialista.xlsx"
# fichdestino2Hoka = destinohoka+"/HOKAFEETURES SS23 Especialista.xlsx"
fichdestinoArena = destinoArena+"/ARENA FW23.xlsx"


fich1Hoka = "c:/Users/onlin/Downloads/HOKA FW23 Especialista.xlsx"
# fich2Hoka = "c:/users/onlin/Downloads/HOKAFEETURES SS23 Especialista.xlsx"
fich1Arena = "c:/users/onlin/Downloads/ARENA FW23.xlsx"


if Path(fich1Hoka).is_file():
    print(fich1Hoka)
    print("ha encontrado el fichero de origen")
else:
    print("NO HA ENCONTRADO EL FICHERO HOKA FW23")    


if Path(fichdestino1Hoka).is_file():
    print("existe fichdestino1 hoka")
    remove(fichdestino1Hoka)
else:
    print("no existe fichdestino1Hoka")


if Path(fichdestinoArena).is_file():
    print("existe fichdestino Arena")
    remove(fichdestinoArena)
else:
    print("no existe fichdestino Arena")


shutil.move(fich1Hoka, destinohoka)
shutil.move(fich1Arena, destinoArena)


