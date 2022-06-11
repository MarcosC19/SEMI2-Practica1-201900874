import logging

# CONFIGURATION LOGGING
logger = logging.getLogger('Semi2-Practica1')
logger.setLevel(logging.DEBUG)

fileLog = logging.FileHandler('logs.log')
fileLog.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileLog.setFormatter(formatter)

logger.addHandler(fileLog)
