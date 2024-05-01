
# 30/4/2024
# 30th April, 2024

class date(object):

    # Could be a dataclass i cant be bothered

    day: int
    month: int
    year: int

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        

    def isValid(self) -> bool:
        
        # Leap years
        isLeapYear = self.isLeapYear()
        if self.month == 2:
            if self.day == 29 and not isLeapYear:
                return False

        monthLengths = {
            1: 31,
            2: (29 if isLeapYear else 28),
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        if self.month > 12 or self.month <= 0:
            return False
        
        if self.day <= 0:
            return False

        if self.day > monthLengths[self.month]:
            return False

        return True



        

        
        
    def isLeapYear(self) -> bool:
        # Every year that is exactly divisible by four is a leap year, 
        # except for years that are exactly divisible by 100,
        #  but these centurial years are leap years if they are exactly divisible by 400. 
        # For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are

        if self.year % 4 != 0:
            return False

        if self.year % 100 == 0:
            if self.year % 400 == 0:
                pass
            else:
                return False
        
        return True
        
        

    def toLongDate(self) -> str:
        day = f"{self.day}{get_ordinal_indicator(self.day)}"

        return f"{day} {month_num_to_string(self.month)}, {self.year}"

    def toShortDate(self) -> str:
        return f"{self.day}/{self.month}/{self.year}"


def get_ordinal_indicator(num: int) -> str:
    d = {1: "st",
        2: "nd",
        3: "rd",
        4: "th",
        5: "th",
        6: "th",
        8: "th",
        9: "th",
        0: "th"}

    return d[num % 10]

def month_num_to_string(month: int) -> str:
    monthsDict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"}
    
    return monthsDict[month]



date(29, 2, 2024).isValid()

