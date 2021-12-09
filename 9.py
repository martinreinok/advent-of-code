data9 = [x.strip() for x in open(f"puzzle_input/9")]
print(data9)
low_points = []


# Very messy solution, part 2 wasnt that bad

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
import numpy as np
from scipy import ndimage
from collections import Counter

data9 = [[*map(int, x.strip())] for x in open(f"puzzle_input/9")]
data9 = np.array(data9)
data9[data9 < 9] = 1
data9[data9 == 9] = 0
# 0 is for background in scipy.ndimage.label (not considered)
print(f"\n#Minesweeper\n {data9} \n")
connected = ndimage.label(data9)
print(connected)
# connected_sizes = Counter(connected)  # nop
unique, counts = np.unique(connected[0], return_counts=True)
counts = np.sort(np.delete(counts, 0))  # delete 0 and sort
print(counts)
print("part2:", counts[-1] * counts[-2] * counts[-3])
