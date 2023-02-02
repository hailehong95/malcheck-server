import sys
import logging

from minio_api.config import MINIO_SERVICE_LOG_FILE

logger = logging.getLogger()
logFormatter = logging.Formatter('%(asctime)s - %(filename)s.%(funcName)s:%(lineno)d - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

fileHandler = logging.FileHandler(MINIO_SERVICE_LOG_FILE)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
