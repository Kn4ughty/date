import sys
import re

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
    12: "December"
}

reversedMonthsDict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}



class date(object):
    day: int
    month: int
    year: int

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        

    def isValid(self) -> bool:
        # Leap years
        if self.month == 2:
            if self.day == 29 and not (isLeapYear := self.isLeapYear()):
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
        # Reference material
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
    return monthsDict[month]


def longStrToDate(i: str, checkDate: bool = True) -> date | str:
    #"10th May, 2024"
    
    i = i.split(" ")
    if len(i) < 3:
        return "Could not seperate"

    try:
        day = int(re.match("\\d+", i[0]).group(0))
    except ValueError:
        return "Couldnt int the day"
    except AttributeError:
        return "Day did not match regex"


    try:
        monthStr = re.match("[a-zA-Z]+", i[1]).group(0)
    except AttributeError:
        return "Year did not match regex"

    month = reversedMonthsDict[monthStr]
    
    try:
        year = int(i[2])
    except ValueError:
        return "Couldnt int the year"

    d = date(day, month, year)

    if not d.isValid() and checkDate:
        return "Was not a valid date"

    return d
    
def longStrToShortString(i: str) -> str:
    
    d = longStrToDate(i)

    if isinstance(d, str):
        return f"Invalid {d}"

    return d.toShortDate()

def shortStringToDate(i: str) -> date | str:
    # 10/5/2024
    i = i.split("/")
    
    try:
        day = int(i[0])
        month = int(i[1])
        year = int(i[2])
    except ValueError:
        return "failed to turn into int"

    d = date(day, month, year)

    if not d.isValid():
        return "Valid date was not given"
    
    return d

def shortStringToLongString(i: str) -> str:
    d = shortStringToDate(i)

    if isinstance(d, str):
        return f"Invalid {d}"

    return d.toLongDate()


try:
    f = sys.argv[1]
except IndexError:
    f = ""

def main():
    i = input("#: ")
    while True:
        if f == "l-s":
            print(longStrToShortString(i))
        elif f == "s-l":
            print(shortStringToLongString(i))
        elif f == "":
            print("no Args supplied. Quitting")
            sys.exit()
        else:
            print("Invalid argument. assuming s-l")
            print(shortStringToLongString(i))
        
        i = input("#: ")


if __name__ == "__main__":
    main()