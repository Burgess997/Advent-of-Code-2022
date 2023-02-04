# https://adventofcode.com/2022/day/3


def rucksack(sacks):
    sortedGroups = []
    currentGroup = []
    badges = []
    while len(sacks) > 0:
        while len(currentGroup) != 3:
            currentGroup.append(sacks.pop())
        sortedGroups.append(currentGroup)
        currentGroup = []
    for sortedGroup in sortedGroups:
        for item in sortedGroup[0]:
            if item in sortedGroup[1] and item in sortedGroup[2]:
                badges.append(item)
                break
    return sum([getLetterPriority(a) for a in badges])


def getLetterPriority(letter):
    if ord(letter) >= 97:
        return ord(letter) - 96
    return ord(letter) - 38

with open("input.txt", "r") as input:
    sacks = [a.strip("\n") for a in input.readlines()]

print(rucksack(sacks))

# Testing
# print(rucksack(["vJrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg",
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw"]))

