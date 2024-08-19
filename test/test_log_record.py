import unittest
from src.log_record import LogRecord


class TestLogRecord(unittest.TestCase):
    def test_init(self):
        record = LogRecord({
            "version": 2,
        }, "tag")
        self.assertIsInstance(record.fields, dict)
        self.assertIsInstance(record.tag, str)


if __name__ == "__main__":
    unittest.main()
