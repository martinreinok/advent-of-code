"""
2021
Day 1 of Advent of Code
https://adventofcode.com/
"""

data = [int(x) for x in open(f"puzzle_input/1")]


def part_one(data_list):
    is_larger = 0
    previous = 0
    for each in data_list:
        if each > previous:
            is_larger += 1
            print(f"{each} is larger than {previous}")
        else:
            print(f"{each} is NOT larger than {previous}")
        previous = each
    print(f"Answer: {is_larger - 1}")
    return {is_larger - 1}


def part_two(data_list):
    element_number = 0
    data_2 = []
    while element_number < 1998:
        avg = (data_list[element_number] + data_list[element_number + 1] + data_list[element_number + 2]) / 3
        data_2.append(avg)
        element_number += 1
    answer = part_one(data_2)
    return answer


part_one_answer, part_two_answer = part_one(data), part_two(data)

print(f"Part one answer: {part_one_answer}\nPart two answer: {part_two_answer}")
