data = [[int(y) for y in x.strip().split(" ")] for x in open(f"puzzle_input/02")]
print(data)

def part_one():
    safe_route = 0
    for route in data:
        for counter, number in enumerate(route):
            next_number = route[counter + 1]

            print(counter, number)
            # Check at least one and at most three, no equal digits.
            if abs(number - next_number) > 3 or abs(number-next_number) == 0:
                print(f"Unsafe route: {route}")
                break
            # Check for all decrease
            if route[0] < route[1] and number - next_number > 0:
                print(f"Unsafe route: {route}")
                break
            # Check for all increase
            if route[0] > route[1] and number - next_number < 0:
                print(f"Unsafe route: {route}")
                break
            if counter >= len(route) - 2:
                safe_route += 1
                break
    return safe_route

def part_two():
    safe_route = 0
    for route in data:
        for counter, number in enumerate(route):
            next_number = route[counter + 1]
            # next_next_number = route[counter + 2]

            # Check at least one and at most three, no equal digits.
            if abs(number - next_number) > 3 or abs(number-next_number) == 0:
                print(f"Unsafe route: {route}")
                break
            # Check for all decrease
            if route[0] < route[1] and number - next_number > 0:
                print(f"Unsafe route: {route}")
                break
            # Check for all increase
            if route[0] > route[1] and number - next_number < 0:
                print(f"Unsafe route: {route}")
                break
            if counter >= len(route) - 2:
                safe_route += 1
                break
    return safe_route

print(f"Part one answer: {part_one()}\nPart two answer: {part_two()}")
