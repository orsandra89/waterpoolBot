import os
import logging
from logging import config as logging_config

here = os.path.abspath(os.path.dirname(__file__))
LOGGING_CONFIG = os.path.abspath(os.path.join(here, 'config.ini'))

logging_config.fileConfig(LOGGING_CONFIG)

app_logger = logging.getLogger('app')

