import csv
from .log_record import LogRecord


def parse_lookup_table(table: str) -> list[LogRecord]:
    reader = csv.DictReader(table.splitlines())
    records = []
    for row in reader:
        record = LogRecord()
        records.append(record)
    return records
