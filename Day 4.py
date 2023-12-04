import re
from typing import Iterable

from functions import getExample, getInputs, getTest

cardsIntances:dict[int, int] = {}
cardsLuckyNumbers:dict[int, int] = {}
totalScratches:int = 0

def getCard(lineIndex:int, line: str):
    sides = line.split(':')[1].split('|')
    
    regex = r'\b\d+\b'
    winningNumbers = re.findall(regex, sides[0])
    numbersIHave = re.findall(regex, sides[1])

    luckyNumbers=[]

    for numberIHave in numbersIHave:
        if numberIHave in winningNumbers:
            luckyNumbers.append(numberIHave)

    cardsLuckyNumbers[lineIndex + 1]=len(luckyNumbers)

    return luckyNumbers

def countPoints(luckyNumbers:list):
    numberOfLuckyNumbers = len(luckyNumbers)
    if numberOfLuckyNumbers == 0:
        return 0
    
    if numberOfLuckyNumbers == 1:
        return 1
    
    total = 1
    for i in range(1, numberOfLuckyNumbers):
        total*=2

    return total

def redeemCard(gameNumber:int):     
    for i in range(1, cardsLuckyNumbers[gameNumber]+1):
        gameNumberToIncrement = gameNumber + i

        if cardsIntances.get(gameNumberToIncrement):
            cardsIntances[gameNumberToIncrement] = cardsIntances[gameNumberToIncrement] + 1
        else:
            cardsIntances[gameNumberToIncrement] = 1
    # print(f'after redeeming {gameNumber}: {cardsIntances}')
    
def scratchCard(gameNumber:int, isOriginal:bool):
    
    global totalScratches
    totalScratches = totalScratches + 1

    if isOriginal:
        return
    
    if cardsIntances.get(gameNumber):
        cardsIntances[gameNumber] = cardsIntances[gameNumber] - 1


def firstPart(file:Iterable[str]):
    total = 0
    for lineIndex, line in enumerate(file):
        luckyNumbers = getCard(lineIndex, line)
        print(f'Card {lineIndex+1}: {luckyNumbers}')
        cardPoints = countPoints(luckyNumbers)
        print(f"Card {lineIndex+1}: {cardPoints}")
        total+=cardPoints
    
    print(f'Total: {total}')


def secondPart(file:Iterable[str]):
    for lineIndex, line in enumerate(file):
        cardNumber = lineIndex + 1 
        getCard(lineIndex, line)

        scratchCard(cardNumber, True)
        redeemCard(cardNumber)

        if cardsIntances.get(cardNumber):
            for i in range(1, cardsIntances[cardNumber]+1):
                # print(f'Scratching card instance {cardNumber} for the nth {i}')
                scratchCard(cardNumber, False)
                redeemCard(cardNumber)

        # print(f"Card {cardNumber} scratches: {totalScratches}")
        # print(f'Instances for card {cardNumber}: {cardsIntances}')
    
    print(f'Total: {totalScratches}')


totalScratched:int = 0
def scratch(line: str, burst: list[int]):
    sides = line.split(':')[1].split('|')
    
    regex = r'\b\d+\b'
    winningNumbers = re.findall(regex, sides[0])
    numbersIHave = re.findall(regex, sides[1])

    if len(burst) == 0:
        burst.append(0)

    burstValue = burst.pop(0) + 1

    winningNumberIndex = 0
    for numberIHave in numbersIHave:
        if numberIHave in winningNumbers:
            if len(burst) <= winningNumberIndex:
                burst.append(0)
            burst[winningNumberIndex] = burst[winningNumberIndex] + burstValue
            winningNumberIndex = winningNumberIndex + 1


    global totalScratched
    totalScratched += burstValue

    return burst

def secondPartV2(file:Iterable[str]):
    burst = []
    for line in file:
        burst = scratch(line, burst)

    print(f'Total: {totalScratched}')



# firstPart(getExample(4)) 
# firstPart(getInputs(4))
# secondPart(getExample(4)) 
# secondPart(getTest(4)) 
# secondPart(getExample(4)) 
# secondPartV2(getTest(4)) 
# secondPartV2(getExample(4)) 
secondPartV2(getInputs(4)) 