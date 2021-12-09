data9 = [x.strip() for x in open(f"puzzle_input/9")]
print(data9)
low_points = []


def check_neighbours(datalist, checkrow, checkindex):
    if datalist[i + checkrow][n] > datalist[i][n] < datalist[i][n + checkindex]:
        return True
    else:
        return False


# Part 1
for i in range(0, len(data9)):
    for n in range(0, len(data9[i])):
        # Corners checking
        # print(f"n: {n}, i: {i}, nr: {data9[i][n]}")
        if i == 0:
            if n == 0:
                if check_neighbours(data9, 1, 1):
                    low_points.append(data9[i][n])
            elif n == len(data9[i]) - 1:
                if check_neighbours(data9, 1, -1):
                    low_points.append(data9[i][n])
            else:
                if check_neighbours(data9, 1, 1) and check_neighbours(data9, 1, -1):
                    low_points.append(data9[i][n])

        elif i == len(data9) - 1:
            if n == 0:
                if check_neighbours(data9, -1, 1):
                    low_points.append(data9[i][n])
            if n == len(data9[i]) - 1:
                if check_neighbours(data9, -1, -1):
                    low_points.append(data9[i][n])
            else:
                if check_neighbours(data9, -1, 1) and check_neighbours(data9, -1, -1):
                    low_points.append(data9[i][n])

        elif n == 0:
            if check_neighbours(data9, -1, 1) and check_neighbours(data9, 1, 1):
                low_points.append(data9[i][n])

        elif n == len(data9[i]) - 1:
            if check_neighbours(data9, -1, -1) and check_neighbours(data9, 1, -1):
                low_points.append(data9[i][n])
        else:
            if check_neighbours(data9, -1, -1) and check_neighbours(data9, 1, 1):
                low_points.append(data9[i][n])

low_points = [int(x) for x in low_points]
print("Low points:", low_points)
print("Risk level:", sum(low_points) + len(low_points))

# Part 2
