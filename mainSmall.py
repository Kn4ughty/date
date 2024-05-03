import sys, re
monthsDict, reversedMonthsDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}, { "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
class date(object):
    def __init__(self, day: int, month: int, year: int):
        self.day, self.month, self.year = day, month, year
    def isValid(self) -> bool:
        monthLengths = { 1: 31, 2: (29 if (False if (self.year % 4 != 0) or (self.year % 100 == 0 and not self.year % 400 == 0) else True) else 28), 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,}
        return False if self.month == 2 and self.day == 29 and not (False if (self.year % 4 != 0) or (self.year % 100 == 0 and not self.year % 400 == 0) else True) or (self.month > 12 or self.month <= 0) or (self.day <= 0) or (self.day > monthLengths[self.month]) else True
def longStrToDate(i: str, checkDate: bool = True) -> date | str:
    i = i.split(" ")
    if len(i) < 3:
        return "Could not seperate"
    try:
        day = int(re.match("\\d+", i[0]).group(0))
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
    return "Valid date was not given" if not date(day, month, year).isValid() else date(day, month, year)
def shortStringToDate(i: str) -> date | str:
    i = i.split("/")
    try:
        day, month, year = int(i[0]), int(i[1]), int(i[2])
    except ValueError:
        return "failed to turn into int"
    return "Valid date was not given" if not date(day, month, year).isValid() else date(day, month, year)
f = sys.argv[1] if len(sys.argv) > 1 else "s-l"
def noargs():
    print("no Args supplied. Quitting")
    sys.exit()
if __name__ == "__main__":
    while True:
        i = input("#: ")
        print(f"Invalid {longStrToDate(i)}"if isinstance(longStrToDate(i), str) else f"{longStrToDate(i).day}/{longStrToDate(i).month}/{longStrToDate(i).year}") if f == "l-s" else print(f"Invalid {shortStringToDate(i)}" if isinstance(shortStringToDate(i), str) else f"{shortStringToDate(i).day}{ {1: "st", 2: "nd", 3: "rd", 4: "th", 5: "th", 6: "th", 8: "th", 9: "th", 0: "th"}[shortStringToDate(i).day % 10]} {monthsDict[shortStringToDate(i).month]}, {shortStringToDate(i).year}") if f == "s-l" else noargs() if f == "" else print(f"Invalid {shortStringToDate(i)}" if isinstance(shortStringToDate(i), str) else f"{shortStringToDate(i).day}{ {1: "st", 2: "nd", 3: "rd", 4: "th", 5: "th", 6: "th", 8: "th", 9: "th", 0: "th"}[shortStringToDate(i).day % 10]} {monthsDict[shortStringToDate(i).month]}, {shortStringToDate(i).year}")