import unittest
from kates import *


class TestKate(unittest.TestCase):
    def test___init__(self):
        kate1 = Kate("Test")
        kate2 = Kate("Test")
        print(kate1)
        print(repr(kate1))
        kates = [kate1, kate2]
        print(kates)
        self.assertEqual(repr(kate1), repr(kate2))
        self.assertEqual(str(kate1), str(kate2))
        self.assertIsNot(kate1, kate2)

    def test_susilauzyti_koja(self):
        kate = Kate("Test")
        kate.susilauzyti_koja()
        self.assertEqual(kate.kojos, 3)

    def test_sugydyti_koja(self):
        kate = Kate("Test")
        kate.susilauzyti_koja()
        kate.sugydyti_koja()
        self.assertEqual(kate.kojos, 4)

if __name__ == "__main__":
    unittest.main()
