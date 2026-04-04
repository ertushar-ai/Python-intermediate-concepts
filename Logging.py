# Logging: Block Level, Configuration options, modules, Lock handlers, Stack traces and Rotating files
# use this link to read more about attributes : https://docs.python.org/3/library/logging.html#logrecord-attributes

import logging

# Can only be ran one time!
logging.basicConfig(
    level=logging.DEBUG,  # defines from which level logging should start
    format="%(asctime)s - %(name)s- %(levelname)s - %(message)s",  # formatting the logger
    datefmt="%d/%m/%y %H:%M:%S",  # date formatting
    filename="New.log",  # file name, in which logs should be saved
    filemode="w",  # file mode
)


logging.debug("This is a debug message") # Level 1
logging.info("This is an info message") # Level 2
logging.warning("This is a warning message") # Level 3  #By default the logger will show the value in warning and above of its level
logging.error("This is an error message") # Level 4
logging.critical("This is a critical message") # Level 5


x = 2
logging.debug(f"The value of x is: {x}")  # used log the value of variable


try:
    1 / 0
except ZeroDivisionError:
    logging.error("Zero division error", exc_info=True) # one way to get traceback and error in logging
except ZeroDivisionError as e:
    logging.exception(e) # OR you can use this


# Custom logger
logger = logging.getLogger("New logger")  # name of new logger
handler = logging.FileHandler("new_logger.log")  # file name where new logs should be saved also the default file type is append "a", use mode="w" to override
formatter = logging.Formatter("%(asctime)s - %(name)s- %(levelname)s - %(message)s")  # formatter goes into handler and then handler goes into logging, easy way to understand
handler.setFormatter(formatter)  # assigning formatter to handler
logger.addHandler(handler)  # assigning handler to logger
logger.debug("testing")