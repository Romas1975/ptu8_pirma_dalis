import unittest
from keliamieji import *


class TestKeliamieji(unittest.TestCase):

    # def test_ar_keliamieji(self):
    #     rezultatas = ar_keliamieji(2000)
    #     lukestis = True
    #     self.assertEqual(rezultatas, lukestis)

    # def test_ar_keliamieji(self):
    #     self.assertEqual(ar_keliamieji(2000), True)
    #     self.assertEqual(ar_keliamieji(2020), True)
    #     self.assertEqual(ar_keliamieji(2100), False)

    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(2000))
        self.assertTrue(ar_keliamieji(2020))
        self.assertFalse(ar_keliamieji(2100))


if __name__ == "__main__":
    unittest.main()
