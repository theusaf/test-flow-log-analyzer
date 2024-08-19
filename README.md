# Flow Log Analyzer

Given a CSV file specifying a list of ports, protocols and a tag, the program reads a log file, tags matching log entries and outputs the tag counts and match counts.

## Requirements

- Python 3.11+

## Installation

1. Clone or download the repository

## Usage

```bash
python3 main.py <input_file> <lookup_file>
```

## Notes

Tests were written to ensure functionality of matching logs with lookup data and parsing logs and lookup CSV data. See the [`test`](./test) directory for details.

The code is structured in a way which makes the program easily extensible for matching other log fields.

## Assumptions

- Only supports [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html) in the default version 2 format
- Input will be an ASCII file with a single flow log record per line
- Input 2 will be a CSV file
  - The first row is a header row
  - The columns are [dstport, protocol, tag] (case-sensitive)
    - If no header, assume this order
    - If header exists, use order defined by header
  - `protocol` is a lowercase string
