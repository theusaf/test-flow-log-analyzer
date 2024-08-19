# Flow Log Analyzer

## Usage
```bash
python3 src/main.py <input_file> <lookup_file>
```

## Assumptions
- Only supports [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html) in the default version 2 format
- Input will be an ASCII file with a single flow log record per line
- Input 2 will be a CSV file
  - The first row might be a header row
  - The columns are [dstport, protocol, tag]
    - If no header, assume this order
    - If header exists, use order defined by header
