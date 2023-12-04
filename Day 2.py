from typing import Iterable

from functions import getExample, getInputs

def getGameCubesMaxCountMax(line: str):
    gameSets = line.split(':')[1].split(';')
    cubesMap = {}

    for gameSet in gameSets:
        cubes = gameSet.split(', ')
        
        for cube in cubes:
            countCube= cube.split()
            count = int(countCube[0])
            cubesMap.setdefault(countCube[1], count)
           
            if cubesMap.get(countCube[1]) < count:
                cubesMap[countCube[1]]= count
    
    return cubesMap

def firstPart(file:Iterable[str]):

    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    possibles=0
    for index, line in enumerate(file):
        game = getGameCubesMaxCountMax(line)
        possible = True
        
        for maximum in constraints:
            if game.get(maximum) > constraints[maximum]:
                possible = False
        
        if possible:
            possibles+=index+1
    
    print(f'Sum of possible indexes is {possibles}')
    
    return possibles


def secondPart(file:Iterable[str]):
    totalPower = 0
    for index, line in enumerate(file):
        game = getGameCubesMaxCountMax(line)
        power = 1

        for cube in game:
            power*=game.get(cube)
        
        print(f'Game {index + 1} has a power of {power}. Cubes: {game}')
        totalPower+=power
        
    print(f'Total power is {totalPower}')
    return totalPower




firstPart(getExample(2)) 
secondPart(getExample(2)) 
firstPart(getInputs(2)) 
secondPart(getInputs(2)) 