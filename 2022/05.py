from copy import deepcopy

containers, steps = open(f"puzzle_input/05.txt").read().split("\n\n")
containers = containers.replace("[", "").replace("]", "").replace("    ", "  ")
containers = containers.split("\n")
columns = containers.pop()
columns = [int(x) for x in columns.split() if x.isdigit()]
crates = {}
for i in range(0, max(columns)):
	crates[i] = []
for row in containers:
	for index, column in enumerate(row):
		if index % 2 == 0:
			crates[index // 2].append(column)

# remove empty slots and append null to end so the array couldn't disappear when emptied
for i in crates:
	crates[i] = [x for x in crates[i] if x != " "]
	crates[i].append("null")
crates_copy = deepcopy(crates)

steps = steps.split("\n")
for index, line in enumerate(steps):
	steps[index] = [int(x) for x in line.split() if x.isdigit()]

for index, step in enumerate(steps):
	for i in range(0, step[0]):
		crates[step[2]-1].insert(0, crates[step[1]-1][0])
		crates[step[1] - 1].pop(0)

print(f"Part 1:")
for i in crates:
	print(crates[i])

for index, step in enumerate(steps):
	for i in range(0, step[0]):
		if step[0] > 1:
			crates_copy[step[2] - 1].insert(0, crates_copy[step[1] - 1][step[0]-i-1])
			crates_copy[step[1] - 1].pop(step[0]-i-1)
		else:
			crates_copy[step[2]-1].insert(0, crates_copy[step[1]-1][0])
			crates_copy[step[1] - 1].pop(0)

print(f"Part 2:")
for i in crates_copy:
	print(crates_copy[i])
