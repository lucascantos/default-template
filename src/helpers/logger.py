import logging
import json
from src.configs.general import LOG_LEVEL

# Create and configure logger
log_format = {
    "Level": "%(levelname)s",
    "Message": "%(message)s",
}
logging.basicConfig(format=json.dumps(log_format))
# Creating an object
log = logging.getLogger()
# Setting the threshold of logger to INFO
log.setLevel(LOG_LEVEL)
