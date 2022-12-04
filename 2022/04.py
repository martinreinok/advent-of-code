data = [x.strip().split(",") for x in open(f"puzzle_input/04.txt")]
data = [x.split("-") for y in data for x in y]
data = [int(x) for y in data for x in y]

pair_data = []
for index, element in enumerate(data):
	if not index % 2 == 0:
		continue
	pair_data.append([data[index], data[index + 1]])

answer = 0
for index, pair in enumerate(pair_data):
	if not index % 2 == 0:
		continue
	if pair[0] in range(pair_data[index+1][0], pair_data[index+1][1]+1) and pair[1] in range(pair_data[index+1][0], pair_data[index+1][1]+1):
		answer += 1
	elif pair_data[index+1][0] in range(pair[0], pair[1]+1) and pair_data[index+1][1] in range(pair[0], pair[1]+1):
		answer += 1
print(f"Part 1: {answer}")

answer2 = 0
for index, pair in enumerate(pair_data):
	if not index % 2 == 0:
		continue
	if pair[0] in range(pair_data[index+1][0], pair_data[index+1][1]+1) or pair[1] in range(pair_data[index+1][0], pair_data[index+1][1]+1):
		answer2 += 1
	elif pair_data[index + 1][0] in range(pair[0], pair[1] + 1) or pair_data[index + 1][1] in range(pair[0], pair[1] + 1):
		answer2 += 1

print(f"Part 2: {answer2}")
