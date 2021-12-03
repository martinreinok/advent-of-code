"""
2021
Day 3 of Advent of Code
https://adventofcode.com/
"""


# Probably overthinked this a bit

def read_lines_from_file(filename):
    with open(f"puzzle_input/{filename}") as data:
        filedata = []
        for line in data:
            filedata.append(line.strip())
    return filedata


def part_one(data):
    """

    :param data:
    :return: counter of [[amount of 1, amount of 0], [...1, ...0]]
    """
    element_counter = []
    for element in data[0]:
        element_counter.append([0, 0])
    for line in data:
        row_number = 0
        for element in line:
            if element == "0":
                element_counter[row_number][0] += 1
            if element == "1":
                element_counter[row_number][1] += 1
            if row_number < len(data[0]):
                row_number += 1
    return element_counter


def most_common_element_in_data(data, identifier):
    """

    :param data:
    :param identifier:
    :return: more ones than zeroes boolean
    """
    ones = 0
    zeros = 0
    for row in data:
        for element in row[identifier]:
            if element == "1":
                ones += 1
            elif element == "0":
                zeros += 1
    if ones >= zeros:
        ones = True
    else:
        ones = False
    print(f"Most common element in {identifier} is one? {ones}")
    return ones


def part_two(data, common):
    identifier = 0

    if common:
        number1 = "0"
        number2 = "1"
    else:
        number1 = "1"
        number2 = "0"
    for each in data[0]:
        remove = []
        common_element = most_common_element_in_data(data, identifier)
        for row in data:
            if row[identifier] == number1 and common_element:
                remove.append(row)
            elif row[identifier] == number2 and not common_element:
                remove.append(row)
        for i in remove:
            data.remove(i)
        print(common_element, data)
        identifier += 1
        if len(data) == 1:
            return data


data3 = read_lines_from_file("3")
elements_count = part_one(data3)
print(elements_count)
answer_gamma = ""
answer_epsilon = ""
for element in elements_count:
    if element[0] > element[1]:
        answer_gamma += "1"
        answer_epsilon += "0"
    else:
        answer_gamma += "0"
        answer_epsilon += "1"
print("gamma part one: ", answer_gamma)
print("epsilon part one: ", answer_epsilon)
power = int(answer_gamma, 2) * int(answer_epsilon, 2)
print("Power part one:", power)
# Part 2

oxygen = part_two(data3, True)
data3 = read_lines_from_file("3")
co2 = part_two(data3, False)
print(oxygen, co2)
life_support = int(oxygen[0], 2) * int(co2[0], 2)
print(life_support)
