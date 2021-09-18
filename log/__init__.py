import logging

from tracker.config import LOG_PROPS

logging.basicConfig(format=LOG_PROPS.format, level=LOG_PROPS.level)
