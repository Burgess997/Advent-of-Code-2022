# https://adventofcode.com/2022/day/4

def overlappingAssignments(assignments):
    overlappingAssignments = 0
    for assignment in assignments:
        assignmentValue = 0
        if int(assignment[0][0]) > int(assignment[1][1]): assignmentValue += 1
        if int(assignment[0][0]) < int(assignment[1][1]): assignmentValue -= 1
        if int(assignment[0][1]) > int(assignment[1][0]): assignmentValue += 1
        if int(assignment[0][1]) < int(assignment[1][0]): assignmentValue -= 1
        if abs(assignmentValue) != 2: overlappingAssignments = overlappingAssignments + 1
        print(f"{assignment} = {assignmentValue}")
    return overlappingAssignments



with open("input.txt", "r") as input:
    assignments = [[b.split("-") for b in a.strip("\n").split(",")] for a in input.readlines()]

print(overlappingAssignments(assignments))