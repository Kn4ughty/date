

def main():
    inputString = getInput()


def getInput():
    ...


def GetOrdinalIndicator(num: int) -> str:
    d = {1: "st",
        2: "nd",
        3: "rd",
        4: "th",
        5: "th",
        6: "th",
        8: "th",
        9: "th",
        0: "th"}
    
    stringNum = str(num)
    return d[int(stringNum[-1])]


if __name__ == "__main__":
    main()
