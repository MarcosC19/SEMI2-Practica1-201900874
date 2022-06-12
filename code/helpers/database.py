from mysql import connector
from mysql.connector import Error
from .loggerConfig import logger


def startConnection():
    database = connector.connect(
        host="localhost",
        user="root",
        password="Marcos_2021",
        database="semi2_practica1"
    )

    try:
        if database.is_connected():
            cursorQuery = database.cursor()
            cursorQuery.execute("select database();")
            dataDB = cursorQuery.fetchone()
            cursorQuery.close()
            logger.info(f'DB: {dataDB[0]} successfully connected')
    except Error as e:
        logger.error(e)

    return database

# METHOD TO EXECUTE A QUERY WITH A NEW CONNECTION AND CURSOR


def executeQuery(textQuery, type):
    newConnection = startConnection()
    newCursor = newConnection.cursor()
    newCursor.execute(textQuery)

    if type == 'insert':
        newConnection.commit()  # saving query insert

    newCursor.close()
    newConnection.close()

# METHOD TO EXECUTE A QUERY SELECT


def getQuerySelect(textQuery):
    newConnection = startConnection()  # GETTING THE CONNECTION
    cursor = newConnection.cursor()  # DEFINING THE CURSOR TO DO THE QUERY
    cursor.execute(textQuery)  # DOING THE QUERY TO DB

    result = cursor.fetchall()  # MAPPING THE CURSOR RESULT

    cursor.close()
    newConnection.close()

    return result  # RETURN THE RESULT MAPPING
