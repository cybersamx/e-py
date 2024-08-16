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


tcs = [
    AriTestCase(0, 0, 0, 0, 0, math.nan),
    AriTestCase(1, 0, 1, 1, 0, math.inf),
    AriTestCase(0, 1, 1, -1, 0, 0),
    AriTestCase(2, 5, 7, -3, 10, 0.4),
    AriTestCase(5, 2, 7, 3, 10, 2.5),
]


def compare(a: float, b: float) -> bool:
    a_nan = math.isnan(a)
    b_nan = math.isnan(b)

    if a_nan and b_nan:
        return True
    elif a_nan or b_nan:
        return False

    if math.isinf(a) and math.isinf(b):
        return True

    epsilon = 0.00001
    res = math.fabs(a - b)
    return res < epsilon


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        for tc in tcs:
            res = add(tc.a, tc.b)
            expect = tc.addExpected
            self.assertTrue(compare(res, expect))

    def test_subtract(self):
        for tc in tcs:
            res = subtract(tc.a, tc.b)
            expect = tc.subExpected
            self.assertTrue(compare(res, expect))

    def test_multiply(self):
        for tc in tcs:
            res = multiply(tc.a, tc.b)
            expect = tc.mulExpected
            self.assertTrue(compare(res, expect))

    def test_divide(self):
        for tc in tcs:
            try:
                res = divide(tc.a, tc.b)
                expect = tc.divExpected
                self.assertTrue(compare(res, expect))
            except ZeroDivisionError:
                if tc.b == 0:
                    continue


if __name__ == '__main__':
    unittest.main()
