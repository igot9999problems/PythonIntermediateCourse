import logging

# Creating your own logger for your modules. "__name__" is a global variable, it refers to the name of the module.
logger = logging.getLogger(__name__)

# This line will stop propogating, so it won't propogate to the base logger, 
# which means that the main module won't log the message below
# logger.propagate = False

logger.info("Hello from " + logger.name)

