import unittest
from aritmetika import *


class TestAritmetika(unittest.TestCase):

    def test_sudetis(self):
        self.assertEqual(15, sudetis(10, 5))
        self.assertEqual(0, sudetis(-1, 1))
        self.assertEqual(-2, sudetis(-1, -1))

    def test_atimtis(self):
        self.assertEqual(5, atimtis(10, 5))
        self.assertEqual(-2, atimtis(-1, 1))
        self.assertEqual(0, atimtis(-1, -1))

    def test_daugyba(self):
        self.assertEqual(50, daugyba(10, 5))
        self.assertEqual(-1, daugyba(-1, 1))
        self.assertEqual(1, daugyba(-1, -1))

    def test_dalyba(self):
        self.assertEqual(2, dalyba(10, 5))
        self.assertEqual(-1, dalyba(-1, 1))
        self.assertEqual(1, dalyba(-1, -1))
        self.assertEqual(2.5, dalyba(5, 2))
        with self.assertRaises(ZeroDivisionError):
            dalyba(10, 0)

    def test_precision(self):
        dd1 = daugyba(dalyba(10, 3), 3)
        pa3 = sudetis(atimtis(dd1, 3000), 3000)
        pa4 = sudetis(atimtis(pa3, 4050), 4050)
        pa5 = sudetis(atimtis(pa4, 500.0001), 500.0001)
        dd2 = daugyba(dalyba(pa5, 3), 3)
        self.assertEqual(10, dd2)

if __name__ == "__main__":
    unittest.main()
