import logging

# Basic configuration defines the basic settings for the logging level (and above) specified.
# For example, by default, only warning level and above messages are printed. We can change this using the basicConfiguration, 
# with the level as DEBUG. Then it applies to all logging levels, since DEBUG is the lowest logging level.
# By default, the name of the logger is "root"

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %H:%M:%S")

# import helper

# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")


# This is how you can create log handlers. They basically dictate where the logs go. I'll show a stream logger (logs to the console) 
# and a file logger
logger = logging.getLogger(__name__)

# Creating the stream and file handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

# Setting the levels for which we want the handlers to handle (wowwwwwww)
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# Creating the format that we want for these handlers and putting it in a variable
format_desired = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

# Setting the format that we want in both handlers by using the variable we created that has the format we want
stream_h.setFormatter(format_desired)
file_h.setFormatter(format_desired)

# Adding the handlers to the logger so we can start using them
logger.addHandler(stream_h)
logger.addHandler(file_h)

# Now, use the logger as normal, and see what happens
logger.warning("This is a warning message")
logger.error("This is an error message")