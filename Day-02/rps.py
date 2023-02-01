# https://adventofcode.com/2022/day/2

with open("input.txt", "r") as input:
    rpsList = input.readlines()
    rpsList = [a.strip("\n").split(" ") for a in rpsList]
print(rpsList)

scoreDict = {"A" : 1, "B" : 2, "C" : 3,
             "X" : 1, "Y" : 2, "Z" : 3}
resultDict = {["A", "X"] : 3, ["A", "Y"] : 0, ["A", "Z"] : 6,
              ["B", "X"] : 6, ["B", "Y"] : 3, ["B", "Z"] : 0,
              ["C", "X"] : 0, ["C", "Y"] : 6, ["C", "Z"] : 3}