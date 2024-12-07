"""
2024 woo! The best year of my life (so far).
Day 1 of Advent of Code
https://adventofcode.com/
"""

data = [x.strip().split(" ") for x in open(f"puzzle_input/01")]
print(data)
left_list = [int(x[0]) for x in data]
left_list.sort()
right_list = [int(x[3]) for x in data]
right_list.sort()

print(left_list)
print(right_list)

distance = 0
for i, _ in enumerate(left_list):
    distance += abs(left_list[i] - right_list[i])

similarity = 0
for i, _ in enumerate(left_list):
    similarity += left_list[i] * right_list.count(left_list[i])



print(f"Part one answer: {distance}\nPart two answer: {similarity}")
