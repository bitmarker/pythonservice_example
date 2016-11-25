import logging
import logging.handlers

# Set the debug level
logging.basicConfig(level=logging.DEBUG)
# Create a logger
logger = logging.getLogger(__name__)



logger.info('Start pythonservice.py!')
logger.critical('Woouou')

'''
def setupLogging():
    # Set the debug level
    logging.basicConfig(level=logging.DEBUG)
    # Create a logger
    logger = logging.getLogger(__name__)
    # Create a handler
    handler = logging.handlers.SysLogHandler(address='/dev/log')
    # Create a formatter
    formatter = logging.Formatter('%(module)s: <%(levelname)s> %(message)s')
    # Set the formatter
    handler.setFormatter(formatter)
    # Add the handler
    #logger.addHandler(handler)
    # Return the logger
    return logger


syslogger = setupLogging()



syslogger.info('Start pythonservice.py!')
syslogger.critical('Woouou')
'''

