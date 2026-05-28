from src.logger import logger

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")


# # below code is to check the exception config
from src.logger import logger
from src.exception import MyException
import sys

try:
     a = 1+'Z'
except Exception as e:
    logger.info(e)
    raise MyException(e, sys) from e