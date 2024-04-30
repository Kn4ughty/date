import unittest

import dates

class TestStringFormating(unittest.TestCase):

    def testOrdinals(self):
        self.assertEqual(dates.GetOrdinalIndicator(2), "nd")
        self.assertEqual(dates.GetOrdinalIndicator(1), "st")
        self.assertEqual(dates.GetOrdinalIndicator(3), "rd")





if __name__ == "__main__":
    unittest.main()
