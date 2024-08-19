class LogRecord:

    def __init__(self, fields=None, tag=None):
        self.fields = {
            "version": None,
            "account-id": None,
            "interface-id": None,
            "srcaddr": None,
            "dstaddr": None,
            "srcport": None,
            "dstport": None,
            "protocol": None,
            "packets": None,
            "bytes": None,
            "start": None,
            "end": None,
            "action": None,
            "log-status": None
        }
        if fields:
            self.fields.update(fields)
        self.tag = tag
