import logging

# DEBUG:10: Detailed information, typically of interest only when diagnosing problems.

# INFO:20: Confirmation that things are working as expected.

# WARNING:30: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR:40: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL:50: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class StringNotAllowed(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def add(x, y):
    """Add Function"""
    logging.info("adding started")
    try:
        z=x+y
        if type(x) == type(str()) or type(y) == type(str()):
            raise StringNotAllowed("Not Integer Value")
        logging.debug(f"addition is {z}")
    except TypeError as T:
        logging.exception(f"Got an error while addng: {T}")
    except StringNotAllowed as S:
        logging.exception(f"Got an error while addng: {S}")
    else:
        return x + y


def divide(x, y):
    """Divide Function"""
    logging.warning("division started, please dont give 0 number")
    result = None
    try:
        result = x / y
    except ZeroDivisionError:
        logging.exception('Tried to divide by zero')
    except TypeError as T:
        logging.exception(f"Got an error while division: {T}")
    else:
        return result


num_1 = 'b'
num_2 = 'a'

logging.info('operation started')

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

#print(div_result)
