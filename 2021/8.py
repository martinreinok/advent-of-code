data7 = [x.strip() for x in open(f"puzzle_input/8")]
print(data7)
before_delim = [x.split(" | ")[0] for x in open(f"puzzle_input/8")]
after_delim = [x.split(" | ")[1].strip() for x in open(f"puzzle_input/8")]
after_delim = [x.split(" ") for x in after_delim]
print(after_delim)
counter = [0, 0, 0, 0]
# part one
for ii in after_delim:
    for i in ii:
        # number 1
        if len(i) == 2:
            counter[0] += 1
        # number 4
        if len(i) == 4:
            counter[1] += 1
        # number 7
        if len(i) == 3:
            counter[2] += 1
        # number 8
        if len(i) == 7:
            counter[3] += 1
    print(sum(counter))


