from helpers.printMenu import *
from helpers.loggerConfig import logger
from helpers.modelCreation import createModel

def main():
    while True:
        printMenu()
        option = input("Seleccione una opcion: ")
        if option == "1":
            logger.info("Se selecciono la opcion 1 (Crear modelo)")
            createModel()
        elif option == "2":
            logger.info("Se selecciono la opcion 2 (Cargar informacion)")
        elif option == "3":
            logger.info("Se selecciono la opcion 3 (Realizar consultas)")
        elif option == "4":
            logger.info("Se selecciono la opcion 4 (Salir)")
            break
        else:
            logger.error("Se selecciono una opcion no valida")

if __name__ == "__main__":
    logger.info("Aplicacion iniciada")
    main()
    logger.info("Aplicacion finalizada")