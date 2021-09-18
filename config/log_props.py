import logging


class LogProps:
    ENTRY = 'log'

    def __init__(self, parsed_json):
        props = parsed_json[self.ENTRY]
        self.level = getattr(logging, props['level'])
        self.format = props['format']
