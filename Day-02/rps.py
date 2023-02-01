# https://adventofcode.com/2022/day/2

with open("input.txt", "r") as input:
    rpsList = input.readlines()
    rpsList = [a.strip("\n").split(" ") for a in rpsList]
print(rpsList)