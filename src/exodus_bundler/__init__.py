import logging


__version__ = "3.0.0"

root_logger = logging.getLogger(__name__)
root_logger.handlers = [logging.NullHandler()]
