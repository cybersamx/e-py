import unittest
from dataclasses import dataclass

from utils.strings import reverse


class TestStrings(unittest.TestCase):
    def test_reverse(self):
        @dataclass
        class TestCase:
            input: str
            expected: str

        testcases = [
            TestCase('abcdef', 'fedcba'),
            TestCase('1234567890', '0987654321'),
            TestCase('12345abcdef', 'fedcba54321'),
        ]

        for tc in testcases:
            result = reverse(tc.input)
            self.assertEqual(result, tc.expected)


if __name__ == '__main__':
    unittest.main()
