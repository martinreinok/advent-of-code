data7 = [x.split(",") for x in open(f"puzzle_input/7")]
data7 = [int(x) for x in data7[0]]

print(data7)


def align_to_position_p1(current_pos, final_pos):
    return abs(final_pos - current_pos)


def calculate_fuel_cost_p2(current_pos, final_pos):
    fuelcost = 0
    for iii in range(0, int(abs(final_pos - current_pos))+1):
        fuelcost += iii
    return fuelcost


alignment = []
alignment_answers = []
alignment_part2 = []
alignment_answers_part2 = []
average = sum(data7) // len(data7)

# Super inefficient
for i in range(max(data7)):
    print(f"{i}/{max(data7)}")
    for crab in data7:
        # Part one
        alignment.append(align_to_position_p1(crab, i))
        # Part two
        alignment_part2.append(calculate_fuel_cost_p2(crab, i))
    alignment_answers.append(sum(alignment))
    alignment_answers_part2.append(sum(alignment_part2))
    alignment.clear()
    alignment_part2.clear()
print(f"fuel used for position part 1:", min(alignment_answers))
print(f"fuel used for position part 2:", min(alignment_answers_part2))
