import json

from .log_props import LogProps
from .url_props import URLProps

CONFIG_FILE_PATH = 'tracker/config/config.json'


with open(CONFIG_FILE_PATH) as f:
    _jsonobj = json.load(f)
    LOG_PROPS = LogProps(_jsonobj)
    URL_PROPS = URLProps(_jsonobj)
