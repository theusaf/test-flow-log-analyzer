import os
import sys

from src.parse_lookup_table import parse_lookup_table, reverse_protocol_map
from src.log_record import LogRecord
cwd = os.getcwd()


def main():
    input_file = sys.argv[1]
    lookup_file = sys.argv[2]

    input_rows: list[LogRecord] = None
    lookup_rows: list[LogRecord] = None
    with open(input_file, "r") as f:
        input_data = f.readlines()
        input_rows = [LogRecord.parse_line(line) for line in input_data]

    with open(lookup_file, "r") as f:
        lookup_data = f.read()
        lookup_rows = parse_lookup_table(lookup_data)

    # Find matching rows and update its tag
    for row in input_rows:
        for lookup in lookup_rows:
            if lookup == row:
                row.tag = lookup.tag

    # Print results
    tag_counts: dict[str, int] = {}
    untagged_count = 0
    for row in input_rows:
        if row.tag is None:
            untagged_count += 1
        elif row.tag in tag_counts:
            tag_counts[row.tag] += 1
        else:
            tag_counts[row.tag] = 1
    print("Tag Counts:")
    print("Tag,Count")
    for tag, count in tag_counts.items():
        print(f"{tag},{count}")
    print(f"Untagged,{untagged_count}\n")

    match_counts: dict[str, int] = {}
    for row in input_rows:
        if row.tag is None:
            continue
        port = row.fields["dstport"]
        protocol = row.fields["protocol"]
        key = f"{port},{reverse_protocol_map.get(protocol, protocol)}"
        if row.tag in match_counts:
            match_counts[key] += 1
        else:
            match_counts[key] = 1

    print("Port/Protocol Combination Counts:")
    print("Port,Protocol,Count")
    for key, count in match_counts.items():
        print(f"{key},{count}")


if __name__ == "__main__":
    main()
