from logger import logging

def add(a,b):
    logging.debug("Addition is starting.")
    return (a+b)

logging.debug("Addition fucntion calling ...")
add(5,10)