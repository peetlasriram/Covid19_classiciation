from src.Classification import logger
from src.Classification.Exception import CustomException
import sys

logger.info("this is my logging filae")


try:
    a=4
    b="3"
    c=a+b
    print(c)
except Exception as e:
    raise CustomException(e,sys)