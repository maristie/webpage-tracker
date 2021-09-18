class URLProps:
    ENTRY = 'urls'

    def __init__(self, parsed_json):
        self.mapping = {k.upper(): v
                        for k, v in parsed_json[self.ENTRY].items()}
