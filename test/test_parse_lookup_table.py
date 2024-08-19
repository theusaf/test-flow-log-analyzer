import unittest
from src.parse_lookup_table import parse_lookup_table


class TestParseLookupTable(unittest.TestCase):
    def test_returns_list(self):
        table = "dstport,protocol,tag"
        result = parse_lookup_table(table)
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
