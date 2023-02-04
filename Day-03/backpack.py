# https://adventofcode.com/2022/day/3

def getLetterPriority(letter):
    if ord(letter) >= 97:
        return ord(letter) - 96
    return ord(letter) - 38