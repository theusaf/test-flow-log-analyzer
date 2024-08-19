import unittest
from src.parse_lookup_table import parse_lookup_table
from src.log_record import LogRecord


class TestParseLookupTable(unittest.TestCase):
    def test_returns_list(self):
        table = "dstport,protocol,tag"
        result = parse_lookup_table(table)
        self.assertIsInstance(result, list)

    def test_returns_list_of_log_records(self):
        table = """
dstport,protocol,tag
25,tcp,sv_P1
68,udp,sv_P2
""".strip()
        result = parse_lookup_table(table)
        self.assertEqual(len(result), 2)
        for record in result:
            self.assertIsInstance(record, LogRecord)


if __name__ == "__main__":
    unittest.main()
