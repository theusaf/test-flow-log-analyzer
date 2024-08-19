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

    @staticmethod
    def parse_line(line: str) -> "LogRecord":
        fields = line.split()
        return LogRecord({
            "version": fields[0],
            "account-id": fields[1],
            "interface-id": fields[2],
            "srcaddr": fields[3],
            "dstaddr": fields[4],
            "srcport": fields[5],
            "dstport": fields[6],
            "protocol": fields[7],
            "packets": fields[8],
            "bytes": fields[9],
            "start": fields[10],
            "end": fields[11],
            "action": fields[12],
            "log-status": fields[13]
        })
