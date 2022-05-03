import logging
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(f"component.log")
fileHandler.setFormatter(logFormatter)
fileHandler.setLevel(logging.INFO)
rootLogger.addHandler(fileHandler)

erroLogHandler = logging.FileHandler(f"error.log")
erroLogHandler.setFormatter(logFormatter)
erroLogHandler.setLevel(logging.ERROR)
rootLogger.addHandler(erroLogHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.INFO)
rootLogger.addHandler(consoleHandler)

# Test messages
rootLogger.debug("Harmless debug Message")
rootLogger.info("Just an information")
rootLogger.warning("Its a Warning")
rootLogger.error("Did you try to divide by zero")
rootLogger.critical("Internet is down")