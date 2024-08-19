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
            fields={"version": "2", "srcport": "100"}, tag="tag")
        self.assertEqual(record2, record3)
        self.assertNotEqual(record1, record2)
        self.assertNotEqual(record1, record3)


if __name__ == "__main__":
    unittest.main()
