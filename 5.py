import numpy as np
from skimage.draw import line


def get_intersect(a1, a2, b1, b2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1, a2, b1, b2])  # s for stacked
    h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
    l1 = np.cross(h[0], h[1])  # get first line
    l2 = np.cross(h[2], h[3])  # get second line
    x, y, z = np.cross(l1, l2)  # point of intersection
    if z == 0:  # lines are parallel
        return float('inf'), float('inf')
    return x / z, y / z


lines = [x.strip() for x in open(f"puzzle_input/5")]
xy = [x.replace(" ->", "").replace(",", " ").split(" ") for x in lines]
x1, y1, x2, y2 = zip(*xy)
boardsizex = [max([min(x1), max(x1), min(x2), max(x2)])]
boardsizey = [max([min(y1), max(y1), min(y2), max(y2)])]

print(boardsizex, boardsizey)
matrix = np.zeros((int(boardsizex[0]) + 1, int(boardsizey[0]) + 1), dtype=np.uint8)

intersections = []

for i in range(0, len(x1)):
    for linepos in x1[i]:
        if int(x1[i]) == int(x2[i]) or int(y1[i]) == int(y2[i]):
            for j in range(0, len(x1)):
                for lineposj in x1[j]:
                    if int(x1[j]) == int(x2[j]) or int(y1[j]) == int(y2[j]):
                        intersect = get_intersect((int(x1[i]), int(y1[i])), (int(x2[i]), int(y2[i])),
                                                  (int(x1[j]), int(y1[j])), (int(x2[j]), int(y2[j])))
                        if "inf" not in str(intersect):
                            if intersect not in intersections:
                                print("Intersecting points:", (int(x1[i]), int(y1[i])), (int(x2[i]), int(y2[i])),
                                      (int(x1[j]), int(y1[j])), (int(x2[j]), int(y2[j])))
                                print(intersect)
                                intersections.append(intersect)
            """
            xx, yy = line(int(x1[i]), int(y1[i]), int(x2[i]), int(y2[i]))
            print("line:", xx, yy)
            matrix[xx, yy] = 1
            """
print("intersections: ", intersections)
