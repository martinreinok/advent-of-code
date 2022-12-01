data = [x.strip() for x in open(f"puzzle_input/01.txt")]
elf = []
food_rations = []

for i in data:
	if i == "":
		food_rations.append(sum(elf))
		elf = []
	else:
		elf.append(int(i))

print(f"Part 1: ", max(food_rations))
food_carried = 0
for i in range(3):
	food_carried += max(food_rations)
	food_rations.remove(max(food_rations))

print(f"Part 2: ", food_carried)
