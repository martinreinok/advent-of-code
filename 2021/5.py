import numpy as np

lines = [x.strip() for x in open(f"puzzle_input/5")]
xy = [x.replace(" ->", "").replace(",", " ").split(" ") for x in lines]
vents = np.array(xy, "int")
boardsize = np.max(vents) + 1
print("Boardsize:", boardsize)
board = np.zeros((boardsize, boardsize), dtype="int")

for i in range(0, len(vents)):
    x, y = [vents[i][0], vents[i][2]], [vents[i][1], vents[i][3]]

    # Vertical lines
    if x[0] == x[1]:
        board[min(y):max(y)+1, x[0]] += 1

    # Horizontal lines
    elif y[0] == y[1]:
        board[y[0], min(x):max(x)+1] += 1

    # Diagonal lines (part 2)
    else:
        if x[0] > x[1]:
            xcoords = range(x[0], x[1] - 1, -1)
        else:
            xcoords = range(x[0], x[1] + 1)

        if y[0] > y[1]:
            ycoords = range(y[0], y[1] - 1, -1)
        else:
            ycoords = range(y[0], y[1] + 1)
        for xx, yy in zip(ycoords, xcoords):
            board[xx, yy] += 1
print(board)
print("Answer:", np.count_nonzero(board > 1))
