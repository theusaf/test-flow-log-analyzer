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

    def test_fields_are_set(self):
        table = """
dstport,protocol,tag
25,tcp,sv_P1
68,udp,sv_P2
""".strip()
        result = parse_lookup_table(table)
        self.assertEqual(result[0].fields["dstport"], "25")
        self.assertEqual(result[0].fields["protocol"], "6")
        self.assertEqual(result[0].tag, "sv_P1")
        self.assertEqual(result[1].fields["dstport"], "68")
        self.assertEqual(result[1].fields["protocol"], "17")
        self.assertEqual(result[1].tag, "sv_P2")

    def test_fields_are_case_insensitive(self):
        table = """
dstport,protocol,tag
25,TCP,sv_P1
68,UDP,sv_P2
""".strip()
        result = parse_lookup_table(table)
        self.assertEqual(result[0].fields["dstport"], "25")
        self.assertEqual(result[0].fields["protocol"], "6")
        self.assertEqual(result[0].tag, "sv_P1")
        self.assertEqual(result[1].fields["dstport"], "68")
        self.assertEqual(result[1].fields["protocol"], "17")
        self.assertEqual(result[1].tag, "sv_P2")


if __name__ == "__main__":
    unittest.main()
