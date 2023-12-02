from io import TextIOWrapper

def getInputs(day:int, part:int=None, example:bool=False) -> TextIOWrapper:
    partPath = ""
    if part is not None:
        partPath=f' part {part}'

    if example is True:
        partPath+=" example"
    return open(f"inputs\\day {day}{partPath}.txt", "r")

def getExample(day:int, part:int=None) -> TextIOWrapper:
    return getInputs(day, part, True)