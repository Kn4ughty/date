import unittest

import dates

class TestStringFormating(unittest.TestCase):

    def testOrdinals(self):
        self.assertEqual(dates.GetOrdinalIndicator(2), "nd")
        self.assertEqual(dates.GetOrdinalIndicator(1), "st")
        self.assertEqual(dates.GetOrdinalIndicator(3), "rd")



    def testPrintLongDate(self):
        self.assertEqual(dates.ShortToLongDate([1, 1, 2000]), "1st January, 2000")
        self.assertEqual(dates.ShortToLongDate([22, 12, 1]), "22nd December, 1")


if __name__ == "__main__":
    unittest.main()
