# https://adventofcode.com/2022/day/2

with open("input.txt", "r") as input:
    rpsList = input.readlines()
    rpsList = [a.strip("\n").split(" ") for a in rpsList]

scoreDict = {"X" : 1, "Y" : 2, "Z" : 3}

# X/A = Rock
# Y/B = Paper
# Z/C = Scissors

resultDict = {"AX" : 3, "AY" : 6, "AZ" : 0,
              "BX" : 0, "BY" : 3, "BZ" : 6,
              "CX" : 6, "CY" : 0, "CZ" : 3}

def rpsScoreCalculator(strategyGuide):
    score = [scoreDict[a[1]] + resultDict["".join(a)] for a in strategyGuide]
    return sum(score)

print(rpsScoreCalculator(rpsList))