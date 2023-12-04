from io import TextIOWrapper

def getInputs(day:int, part:int=None, suffix=None) -> TextIOWrapper:
    partPath = ""
    if part is not None:
        partPath=f' part {part}'

    if suffix is not None:
        partPath+=f" {suffix}"
    return open(f"inputs\\day {day}{partPath}.txt", "r")

def getExample(day:int, part:int=None) -> TextIOWrapper:
    return getInputs(day, part, "example")

def getTest(day:int, part:int=None) -> TextIOWrapper:
    return getInputs(day, part, "test")