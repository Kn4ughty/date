

class date(object):

    # Could be a dataclass i cant be bothered

    day: int
    month: int
    year: int

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
