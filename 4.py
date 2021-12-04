"""
2021
Day 4 of Advent of Code
https://adventofcode.com/
"""
import math


def read_lines_from_file(filename, convert_int):
    if convert_int:
        return [int(x) for x in open(f"puzzle_input/{filename}")]
    else:
        return [x.strip().split() for x in open(f"puzzle_input/{filename}")]


lines = read_lines_from_file("4", False)
print(lines)
bingo = str(lines[0][0]).split(",")
lines.pop(0)
lines = [ele for ele in lines if ele != []]

found = []
"""bingo number, table index[1-x], row index[0-4], element index in row[0-4]"""

for element in bingo:
    position = 1
    row = 0
    for each in lines:
        if row > 4:
            row = 0
        if element in each:
            found.append([element, math.ceil(position/5), row,  each.index(element)])
        position += 1
        row += 1

result = []
for each in found:
    print(each)

print(result)


