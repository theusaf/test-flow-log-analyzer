from typing import Union


class LogRecord:

    def __init__(self, fields: dict[str, str] = None, tag: str = None):
        self.fields: dict[str, Union[None, str]] = {
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

    def __eq__(self, other):
        """
        Compare two `LogRecord` objects for equality.
        Only fields that are not `None` in both objects are compared.
        """
        for key in self.fields.keys():
            if self.fields[key] is not None and other.fields[key] is not None:
                if self.fields[key] != other.fields[key]:
                    return False
        return True
