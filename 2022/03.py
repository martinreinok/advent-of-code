data = [x.strip() for x in open(f"puzzle_input/03.txt")]
data_split = [[x[:len(x)//2], x[len(x)//2:]] for x in data]

result_upper = ""
result_lower = ""
for backpack in data_split:
	for item in backpack[0]:
		if item in backpack[1]:
			if item.islower():
				result_lower += item
			else:
				result_upper += item
			break
print(f"Part 1: {sum([ord(x)-96 for x in result_lower]) + sum([ord(x)-38 for x in result_upper])}")

result_upper = ""
result_lower = ""
index = 0
while index <= len(data) - 2:
	backpack = data[index]
	# index % 3 == 0
	for item in backpack:
		if item in data[index+1] and item in data[index+2]:
			if item.islower():
				result_lower += item
			else:
				result_upper += item
			index += 3
			break
print(f"Part 2: {sum([ord(x)-96 for x in result_lower]) + sum([ord(x)-38 for x in result_upper])}")



