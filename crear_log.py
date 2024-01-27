import logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(threadName)s  - %(processName)s - %(levelname)s - %(message)s', 
                    filename='logdescarregues.log', 
                    filemode='a')
print("aki va la segona linia")
logging.info("PROVA DE LOGGIN1")
logging.info("SEGONa linia")


