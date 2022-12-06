data = [x.strip() for x in open(f"puzzle_input/06.txt")]


def find_marker(buffer, characters):
	processed = 0
	for i in buffer:
		processed += 1
		if len(set(buffer[processed - characters:processed])) == characters:
			return processed
	return -1


for i in data:
	print(f"Part 1: {find_marker(i, characters=4)}")
	print(f"Part 2: {find_marker(i, characters=14)}")
