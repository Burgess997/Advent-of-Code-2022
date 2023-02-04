# https://adventofcode.com/2022/day/3


def rucksack(sacks):
    commonItems = []
    for sack in sacks:
        firstCompartment = sack[:int(len(sack) / 2)]
        secondCompartment = sack[int(len(sack) / 2):]
        for item in firstCompartment:
            if item in secondCompartment:
                commonItems.append(item)
                break
    print(commonItems)
    return sum([getLetterPriority(a) for a in commonItems])

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

