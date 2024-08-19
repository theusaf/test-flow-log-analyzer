class LogRecord:

    def __init__(self, fields=None, tag=None):
        self.fields = fields if fields is not None else {}
        self.tag = tag
