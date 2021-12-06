from collections import deque

data6 = [x.split(",") for x in open(f"puzzle_input/6")]
data6 = [int(x) for x in data6[0]]
print(data6)
i = 0
count = 0
while count < 80:
    for i in range(0, len(data6)):
        if data6[i] == 0:
            data6[i] += 6
            data6.append(8)
        else:
            data6[i] -= 1
        i += 1
    count += 1
print("Data 6 lenght", len(data6))

