import re
from typing import Dict, Iterable, List

from functions import getExample, getInputs
from dataclasses import dataclass

@dataclass
class Finding:
    start: int
    end: int
    value: str
    lineIndex: int

    def __hash__(self):
        # You can combine the hash of each attribute
        return hash((self.start, self.end, self.value, self.lineIndex))

partNumbersMap:List[List[Finding]] = {}
symbolsMap:List[List[Finding]] = {}

def mapPartNumbers(lineIndex: int, line: str):
    partNumbersMap[lineIndex] = []
    regex = r'\b\d+\b'
    pattern = re.compile(regex)
    for match in re.finditer(pattern, line):
        s = match.start()
        e = match.end()
        partNumbersMap[lineIndex].append(Finding(s, e, line[s:e], lineIndex))
        print('String match "%s" at %d:%d' % (line[s:e], s, e))
    

def mapSymbols(lineIndex: int, line: str, symbol:str=None):
    symbolsMap[lineIndex] = []

    if symbol is None:
        regex = r'[^\w\d.\n\r]'
    else: 
        regex = r'[\*]'

    pattern = re.compile(regex)
    for match in re.finditer(pattern, line):
        s = match.start()
        symbolsMap[lineIndex].append(Finding(s, s, line[s:s+1], lineIndex))
        print('String match "%s" at %d' % (line[s:s+1], s))
    
def findAdjacents(lineIndex: int, symbolIndex:int):
    adjacents:List[Finding] = []
    for part in partNumbersMap[lineIndex]:
        partNumberSize = len(part.value)

        # print(f'ps {part.start} gt {symbolIndex-1-partNumberSize} | pe {part.end} lt {symbolIndex+1+partNumberSize}')
        if part.start > symbolIndex -1 -partNumberSize and part.end <= symbolIndex + 1 + partNumberSize:
            adjacents.append(part)
    return adjacents

def findAdjacentsForFinding(finding: Finding, onlyIfTwoAdjacents:bool=False):
    adjacents:List[Finding] = []

    print(finding)
    if finding.lineIndex > 0:
        adjacents.extend(findAdjacents(finding.lineIndex -1, finding.start))

    adjacents.extend(findAdjacents(finding.lineIndex, finding.start))

    if finding.lineIndex < len(symbolsMap) - 1:
        adjacents.extend(findAdjacents(finding.lineIndex +1, finding.start))
    
    if not onlyIfTwoAdjacents:
        return adjacents

    if len(adjacents) == 2:
        return adjacents
    return []

def firstPart(file:Iterable[str]):
    for lineIndex, line in enumerate(file):
        mapPartNumbers(lineIndex, line)
        mapSymbols(lineIndex, line)

    # print(partNumbersMap)
    # print(symbolsMap)
    adjacentParts = set()

    for lineIndex in symbolsMap:
        for finding in symbolsMap[lineIndex]:
            adjacentParts = adjacentParts.union(findAdjacentsForFinding(finding))


    selected_list = [int(x.value) for x in adjacentParts]
    print(sorted(selected_list))
    print(sum(selected_list))


def secondPart(file:Iterable[str]):
    for lineIndex, line in enumerate(file):
        mapPartNumbers(lineIndex, line)
        mapSymbols(lineIndex, line, "*")

    # print(partNumbersMap)
    print(symbolsMap)
    adjacentPartsPowers = []
    debugAdjacentParts = []

    for lineIndex in symbolsMap:
        for finding in symbolsMap[lineIndex]:
            adjacentParts = findAdjacentsForFinding(finding, True)
            debugAdjacentParts.extend(adjacentParts)
            if adjacentParts != []:
                print(f'part {int(adjacentParts[0].value)} {int(adjacentParts[1].value)}')
                adjacentPartsPowers.append(int(adjacentParts[0].value) * int(adjacentParts[1].value))


    selected_list = [int(x.value) for x in debugAdjacentParts]
    print(sorted(selected_list))
    print(sum(adjacentPartsPowers))


# mapPartNumbers("467..114..")

# firstPart(getExample(3)) 
# firstPart(getInputs(3))
secondPart(getExample(3)) 
secondPart(getInputs(3)) 