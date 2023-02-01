# https://adventofcode.com/2022/day/2

with open("input.txt", "r") as input:
    rpsList = input.readlines()
    rpsList = [a.strip("\n").split(" ") for a in rpsList]

scoreDict = {"X" : 1, "Y" : 2, "Z" : 3}

resultDict = {"AX" : 3, "AY" : 6, "AZ" : 0,
              "BX" : 0, "BY" : 3, "BZ" : 6,
              "CX" : 6, "CY" : 0, "CZ" : 3}

actionList = ["X", "Y", "Z"]

actionDict = {"X" : -1, "Y" : 0, "Z" : 1}

opponentDict = {"A" : 0, "B" : 1, "C" : 2}

# A = Rock
# B = Paper
# C = Scissors



def rpsScoreCalculator(strategyGuide):
    scoreSum = 0


    def calculateRound(round):
        action = opponentDict[round[0]] + actionDict[round[1]]
        print(action)
        if action == 3:
            action = 0
        return [round[0], actionList[action]]

    def calculateRoundScore(round):
        return scoreDict[round[1]] + resultDict["".join(round)]


    for round in strategyGuide:
        calculatedRound = calculateRound(round)
        scoreSum += calculateRoundScore(calculatedRound)

    
    return scoreSum

print(rpsScoreCalculator(rpsList))