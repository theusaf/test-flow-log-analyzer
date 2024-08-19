import unittest
from src.log_record import LogRecord


class TestLogRecord(unittest.TestCase):
    def test_init(self):
        record = LogRecord({
            "version": 2,
        }, "tag")
        self.assertIsInstance(record.fields, dict)
        self.assertEqual(record.fields["version"], 2)
        self.assertIsInstance(record.tag, str)

    def test_default_init(self):
        record = LogRecord()
        self.assertIsInstance(record.fields, dict)
        self.assertIsNone(record.tag)

    def test_available_fields(self):
        record = LogRecord(tag="tag")
        self.assertListEqual(
            [key for key in record.fields.keys()],
            ["version", "account-id", "interface-id", "srcaddr", "dstaddr", "srcport",
                "dstport", "protocol", "packets", "bytes", "start", "end", "action", "log-status"]
        )

    def test_comparison(self):
        record1 = LogRecord(fields={"version": "2"}, tag="tag")
        record2 = LogRecord(
            fields={"version": "2", "srcport": "100"}, tag="tag2")
        record3 = LogRecord(
            fields={"version": "2", "srcport": "200"}, tag="tag")
        self.assertEqual(record1, record2)
        self.assertEqual(record1, record3)
        self.assertNotEqual(record2, record3)

    def test_parse_line(self):
        line = "2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK"
        record = LogRecord.parse_line(line)
        self.assertIsInstance(record, LogRecord)
        self.assertEqual(record.fields["version"], "2")
        self.assertEqual(record.fields["account-id"], "123456789012")
        self.assertEqual(record.fields["interface-id"], "eni-0a1b2c3d")
        self.assertEqual(record.fields["srcaddr"], "10.0.1.201")
        self.assertEqual(record.fields["dstaddr"], "198.51.100.2")
        self.assertEqual(record.fields["srcport"], "443")
        self.assertEqual(record.fields["dstport"], "49153")
        self.assertEqual(record.fields["protocol"], "6")
        self.assertEqual(record.fields["packets"], "25")
        self.assertEqual(record.fields["bytes"], "20000")
        self.assertEqual(record.fields["start"], "1620140761")
        self.assertEqual(record.fields["end"], "1620140821")
        self.assertEqual(record.fields["action"], "ACCEPT")
        self.assertEqual(record.fields["log-status"], "OK")


if __name__ == "__main__":
    unittest.main()
