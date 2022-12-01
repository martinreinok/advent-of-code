from collections import Counter

data10 = [x.strip() for x in open(f"puzzle_input/10")]
elements = ["()", "[]", "{}", "<>"]

for i in range(0, len(data10)):
    while "()" in data10[i] or "[]" in data10[i] or "{}" in data10[i] or "<>" in data10[i]:
        for element in elements:
            data10[i] = data10[i].replace(element, "")

lines = []
part_two = []
for x in data10:
    if ")" in x or "}" in x or ">" in x or "]" in x:
        lines.append(x)
    else:
        part_two.append(x)

part_one = []
answer = []
for i in lines:
    for ii in [")", "]", "}", ">"]:
        if ii in i:
            part_one.append(i.index(ii))
    if len(part_one) > 1:
        answer.append(i[min(part_one)])
    else:
        answer.append(i[part_one[0]])
    part_one.clear()
answer = Counter(answer)
print("counter:", answer)
part1 = 0

print("part 1 answer: ", answer.get(")")*3 + answer.get("]")*57 + answer.get("}")*1197 + answer.get(">")*25137)
# essentially mirror the strings
part_two_mirrored = [each[::-1] for each in part_two]
for i in range(0, len(part_two_mirrored)):
    part_two_mirrored[i] = part_two_mirrored[i].replace("{", "}")
    part_two_mirrored[i] = part_two_mirrored[i].replace("[", "]")
    part_two_mirrored[i] = part_two_mirrored[i].replace("<", ">")
    part_two_mirrored[i] = part_two_mirrored[i].replace("(", ")")

part_two_answer = []
for x in part_two_mirrored:
    buffer = 0
    counter = Counter(x)
    for each in x:
        buffer = buffer*5
        if each == ")":
            buffer += 1
        elif each == "]":
            buffer += 2
        elif each == "}":
            buffer += 3
        elif each == ">":
            buffer += 4
    part_two_answer.append(buffer)
print("Part 2 answer: ", sorted(part_two_answer)[len(sorted(part_two_answer))//2])


"""
): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
"""