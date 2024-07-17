import logging

# Basic logging setting...

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()

    ]

)

logger=logging.getLogger("Arthematic App")

def add(a,b):
    result=a+b
    logging.debug(f"Adding {a} + {b} = {result}")
    return result

def sub(a,b):
    result=a-b
    logging.debug(f"Subtracting {a}-{b} = {result}")
    return result

def div(a,b):
    try:
        result=a/b
        logging.debug(f"Dividing {a}/{b} = {result}")
        return result
    except Exception as e:
        print(e)


#add(15,5)
#sub(15,5)
#div(15,5)

div(10,0)