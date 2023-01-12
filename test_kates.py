import unittest
from kates import *


class TestKate(unittest.TestCase):

    def setUp(self):
        self.kate1 = Kate("Test")
        self.kate2 = Kate("Test")
        self.kates = [self.kate1, self.kate2]

    def test___init__(self):
        self.assertEqual(repr(self.kate1), repr(self.kate2))
        self.assertEqual(str(self.kate1), str(self.kate2))
        self.assertIsNot(self.kate1, self.kate2)

    def test_susilauzyti_koja(self):
        self.kate1.kojos = 4
        self.kate1.susilauzyti_koja()
        self.assertEqual(self.kate1.kojos, 3)

    def test_sugydyti_koja(self):
        self.kate1.susilauzyti_koja()
        self.kate1.sugydyti_koja()
        self.assertEqual(self.kate1.kojos, 4)

if __name__ == "__main__":
    unittest.main()
