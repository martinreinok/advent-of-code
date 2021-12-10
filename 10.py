from collections import Counter

data10 = [x.strip() for x in open(f"puzzle_input/10")]
elements = ["()", "[]", "{}", "<>"]

for i in range(0, len(data10)):
    while "()" in data10[i] or "[]" in data10[i] or "{}" in data10[i] or "<>" in data10[i]:
        for element in elements:
            data10[i] = data10[i].replace(element, "")

print(data10)
lines = []
for x in data10:
    if ")" in x or "}" in x or ">" in x or "]" in x:
        lines.append(x)
print(lines)
minimum = []
answer = []
for i in lines:
    for ii in [")", "]", "}", ">"]:
        if ii in i:
            minimum.append(i.index(ii))
            print(i[i.index(ii)])
    if len(minimum) > 1:
        answer.append(i[min(minimum)])
    else:
        answer.append(i[minimum[0]])
    minimum.clear()
print(answer)
answer = Counter(answer)
print(answer)
part1 = 0

print("part1 answer", answer.get(")")*3 + answer.get("]")*57 + answer.get("}")*1197 + answer.get(">")*25137)
