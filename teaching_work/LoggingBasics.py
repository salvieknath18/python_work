import logging

# DEBUG:10: Detailed information, typically of interest only when diagnosing problems.

# INFO:20: Confirmation that things are working as expected.

# WARNING:30: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR:40: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL:50: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig( filename='filename.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    """Add Function"""
    logging.info("adding started")
    logging.debug(f"addition is {x+y}")
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    logging.warning("division started, please dont give 0 number")
    result = None
    try:
        result = x / y
    except ZeroDivisionError:
        logging.exception('Tried to divide by zero')
    else:
        return result


num_1 = 20
num_2 = 0

logging.info('operation started')

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

print(div_result)
