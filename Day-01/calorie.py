# https://adventofcode.com/2022/day/1

def FindMostCalories(calorieList):
    currentElf = []
    currentCalorie = ""
    elfList = []

    while(len(calorieList) != 0):
        currentCalorie = calorieList.pop()
        if currentCalorie != "":
            currentElf.append(int(currentCalorie))
            continue
        elfList.append(sum(currentElf))
        currentElf = []
    elfList.sort(reverse=True)
    return elfList[0]

with open("input.txt", "r") as input:
    calorieList = input.readlines()
    calorieList = [a.strip("\n") for a in calorieList]
print(FindMostCalories(calorieList))