import re
from typing import Iterable

from functions import getExample, getInputs


def firstPart(file:Iterable[str]):
	res = 0
	for line in file:
		numbers = [str(i) for i in line if i.isdigit()]		
		numbers = [numbers[i] for i in (0, -1)]

		total = int(''.join(numbers))
		res+=total
	
	print(f'First part result: {res}')
	return res  


def getNumbersFromWordsAndNumbers(line):
	dict = {
		"eightwoneight": ["8","2","1","8"],
		"twoneight": ["2","1","8"],
		"sevenineight": ["7","9","8"],
		"eightwone": ["8","2","1"],
		"eightwo": ["8","2"],
		"oneight": ["1","8"],
		"twone": ["2","1"],
		"threeight": ["3", "8"],
		"fiveight": ["5","8"], 
		"sevenine": ["7","9"],
		"nineight": ["9","8"],
		"one": ["1"],
		"two": ["2"],
		"three": ["3"],
		"four": ["4"], 
		"five": ["5"], 
		"six": ["6"], 
		"seven": ["7"], 
		"eight": ["8"],
		"nine": ["9"]
	}
	stringNumbers = '|'.join(dict.keys())
	regex = rf"{stringNumbers}|\d"
	findings = re.findall(regex, line)
	result = []
	for finding in findings:
		if finding in dict:
			for num in dict[finding]: 
				result.append(num)
		else:
			result.append(finding)

	return result



def secondPart(file:Iterable[str]):
	res = 0
	for line in file:
		numbers = getNumbersFromWordsAndNumbers(line)
		numbers = [numbers[i] for i in (0, -1)]

		total = int(''.join(numbers))
		res+=total

	print(f'Second part result: {res}')
	return res  

		
firstPart(getExample(1, 1))
secondPart(getExample(1, 2))
firstPart(getInputs(1))
secondPart(getInputs(1))
