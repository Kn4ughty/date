import unittest

import main
from main import date

class TestStringFormating(unittest.TestCase):

    def testOrdinals(self):
        self.assertEqual(main.get_ordinal_indicator(2), "nd")
        self.assertEqual(main.get_ordinal_indicator(1), "st")
        self.assertEqual(main.get_ordinal_indicator(3), "rd")


    def testPrintLongDate(self):
        self.assertEqual(date(1, 1, 2000).toLongDate(), "1st January, 2000")
        self.assertEqual(date(22, 12, 1).toLongDate(), "22nd December, 1")

class testDateValidation(unittest.TestCase):

    def testLeapYears(self):
        self.assertTrue(date(29, 2, 2024))
        self.assertTrue(date(29, 2, 1900))
        self.assertFalse(date(29, 2, 1800))
    
    def testDays(self):
        self.assertFalse(date(0, 1, 1))
        self.assertFalse(date(-1, 1, 1))
        self.assertTrue(date(1, 1, 1))
    



if __name__ == "__main__":
    unittest.main()
