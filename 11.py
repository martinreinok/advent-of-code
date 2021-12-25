import numpy as np

matrix = []
for line in open('puzzle_input/11'):
    matrix.append([int(x) for x in line.strip()])

flashes = 0

print(np.matrix(matrix))


def increment_surrounding(matrix_, row, column):
    global flashes
    flashes += 1
    surrounding_elements = [-1, 0, 1]
    if row != 0 and row != len(matrix_) and column != 0 and column != len(matrix_[row]):

        for i in surrounding_elements:
            matrix_[row + i][column + -1] += 1
            if i != 0:
                matrix_[row + i][column + 0] += 1
            matrix_[row + i][column + 1] += 1
    return matrix_


def flash(octopus_array):
    for row_index in range(len(octopus_array)):
        for index in range(len(octopus_array[row_index])):
            if octopus_array[row_index][index] >= 9:
                octopus_array[row_index][index] = 0
                # Add 1 to all octo around
                octopus_array = increment_surrounding(octopus_array, row_index, index)
                octopus_array[row_index][index] = -100000000
            else:
                octopus_array[row_index][index] += 1
    for row_index in range(len(octopus_array)):
        for index in range(len(octopus_array[row_index])):
            if octopus_array[row_index][index] <= 0:
                octopus_array[row_index][index] = 0
    return octopus_array


steps = 1
for _ in range(steps):
    matrix = flash(matrix)
    while max(max(matrix)) > 9:
        # print(np.matrix(matrix))
        matrix = flash(matrix)
    print("Flashes occured:", flashes)
    print(np.matrix(matrix))

