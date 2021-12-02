def read_lines_from_file(filename):
    with open(f"puzzle_input/{filename}") as data:
        filedata = []
        for line in data:
            filedata.append(line.strip())
    return filedata


def part_one(data):
    for line in data:
        print(line)


data3 = read_lines_from_file("3")
part_one(data3)
