"""
2021
Day 2 of Advent of Code
https://adventofcode.com/
"""


def read_lines_from_file(filename):
    with open(f"puzzle_input/{filename}") as data:
        filedata = []
        for line in data:
            filedata.append(line.strip())
    return filedata


def part_one(data):
    """

    :param data: data
    :return: [forward, down, up]
    """
    forward = 0
    down = 0
    up = 0
    for line in data:
        line = line.split()
        if "forward" in line[0]:
            forward += int(line[1])
        elif "down" in line[0]:
            down += int(line[1])
        elif "up" in line[0]:
            up += int(line[1])

    print(forward, down, up)
    return [forward, down, up]


def part_two(data):
    """

    :param data:
    :return: [forward, down, up, aim]
    """
    forward = 0
    down = 0
    aim = 0
    up = 0
    for line in data:
        line = line.split()
        if "down" in line[0]:
            aim += int(line[1])
        elif "up" in line[0]:
            aim -= int(line[1])
        elif "forward" in line[0]:
            forward += int(line[1])
            down += (aim * int(line[1]))
        print(f"horizontal: {forward} aim: {aim} depth: {down - up}")

    return [forward, down, up, aim]


data2 = read_lines_from_file("2")

forward, down, up = part_one(data2)
print("Answer part one:", (down - up) * forward)

forward, down, up, aim = part_two(data2)
print("Answer part two:", forward * down)
