import unittest

import mainSmall
from mainSmall import date

class TestStringFormating(unittest.TestCase):

    def testOrdinals(self):
        self.assertEqual(mainSmall.get_ordinal_indicator(2), "nd")
        self.assertEqual(mainSmall.get_ordinal_indicator(1), "st")
        self.assertEqual(mainSmall.get_ordinal_indicator(3), "rd")


    def testPrintLongDate(self):
        self.assertEqual(date(1, 1, 2000).toLongDate(), "1st January, 2000")
        self.assertEqual(date(22, 12, 1).toLongDate(), "22nd December, 1")

class testDateValidation(unittest.TestCase):

    def testLeapYears(self):
        self.assertTrue(date(29, 2, 2024).isValid())
        self.assertFalse(date(29, 2, 1900).isValid())
        self.assertFalse(date(29, 2, 1800).isValid())
    
    def testDays(self):
        self.assertFalse(date(0, 1, 1).isValid())
        self.assertFalse(date(-1, 1, 1).isValid())
        self.assertTrue(date(1, 1, 1).isValid())
    
    def testMonths(self):
        self.assertFalse(date(1, 0, 1).isValid())
        self.assertFalse(date(1, 13, 1).isValid())
        self.assertFalse(date(1, -1, 1).isValid())

    def testDaysOfMonths(self):
        self.assertTrue(date(30, 4, 1).isValid())
        self.assertFalse(date(31, 4, 1).isValid())
        # Testing every month would take too long

class testStrToStr(unittest.TestCase):
    
    def testLongStrToShortString(self):
        self.assertEqual(mainSmall.longStrToShortString("10th May, 2024"), "10/5/2024")
        self.assertEqual(mainSmall.longStrToShortString("22nd December, 0"), "22/12/0")
        self.assertEqual(mainSmall.longStrToShortString("twafhfh hfdsk k").split(" ")[0], "Invalid")
        # TEST INVALID
        # TODO

    #def testShortStrToLongString(self):
    #    self.assertEqual(mainSmall.shortStringToLongString("10/5/2024"), "10th May, 2024")
    #    self.assertEqual(mainSmall.shortStringToLongString("29/2/4"), "29th February, 4")
    #    self.assertEqual(mainSmall.shortStringToLongString("29/2/2021").split(" ")[0], "Invalid")
        

if __name__ == "__main__":
    unittest.main()

print(f"{{{1: 1}}}")