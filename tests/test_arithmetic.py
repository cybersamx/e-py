import unittest
import math
from dataclasses import dataclass

from pkg_e.arithmetic import (
    add,
    subtract,
    multiply,
    divide,
)


@dataclass
class AriTestCase:
    a: float
    b: float
    addExpected: float
    subExpected: float
    mulExpected: float
    divExpected: float


def compare(a: float, b: float) -> bool:
    epsilon = 0.00001
    return math.fabs(a-b) < epsilon


class TestArithmetic(unittest.TestCase):
    tcs = [
        AriTestCase(0, 0, 0, 0, 0, math.nan),
        AriTestCase(1, 0, 1, 1, 0, math.inf),
        AriTestCase(0, 1, 1, -1, 0, 0),
        AriTestCase(2, 5, 7, -3, 10, 0.4),
        AriTestCase(5, 2, 7, 3, 10, 2.5),
    ]

    def test_add(self):
        for tc in self.tcs:
            res = add(tc.a, tc.b)
            expect = tc.addExpected
            self.assertTrue(compare(res, expect))

    def test_subtract(self):
        for tc in self.tcs:
            res = subtract(tc.a, tc.b)
            expect = tc.subExpected
            self.assertTrue(compare(res, expect))

    def test_multiply(self):
        for tc in self.tcs:
            res = multiply(tc.a, tc.b)
            expect = tc.mulExpected
            self.assertTrue(compare(res, expect))

    def test_divide(self):
        for tc in self.tcs:
            try:
                res = divide(tc.a, tc.b)
                expect = tc.divExpected
                self.assertTrue(compare(res, expect))
            except ZeroDivisionError:
                if tc.b == 0:
                    continue


if __name__ == '__main__':
    unittest.main()
