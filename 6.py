from collections import Counter

DAYS = 256
data6 = [x.split(",") for x in open(f"puzzle_input/6")]
data6 = [int(x) for x in data6[0]]

counter = Counter(data6)
# Sum of fish instead of each instance of fish
fmap = [counter.get(0), counter.get(1), counter.get(2), counter.get(3),
        counter.get(4), counter.get(5), counter.get(6), counter.get(7), counter.get(8)]

fmap = [0 if x is None else x for x in fmap]
buffer = []
print(fmap)

i = 0
while i < DAYS:
    buffer = fmap.copy()
    fmap = [0 for each in fmap]
    # pos 0 goes to pos 8
    fmap[8] = buffer[0]
    # rotate the list
    for ii in range(8):
        fmap[7-ii] = buffer[7-ii+1]
    fmap[6] += buffer[0]
    # print(fmap)
    i += 1
print(f"Answer: After {DAYS} days there are: {sum(fmap)} lanternfish")
