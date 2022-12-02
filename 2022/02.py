data = [x.strip().split(" ") for x in open(f"puzzle_input/02.txt")]

win, lose, draw = 6, 0, 3
rock, paper, scissors = 1, 2, 3


result = 0
for game in data:
	# rock beats scissors, loses to paper
	# scissors beats paper, loses to rock
	# paper beats rock, loses to scissors
	if game[0] == "A" and game[1] == "Y" or game[0] == "B" and game[1] == "Z" or game[0] == "C" and game[1] == "X":
		# Win
		match game[1]:
			case "X":
				result += rock + win
			case "Y":
				result += paper + win
			case "Z":
				result += scissors + win

	if game[0] == "A" and game[1] == "X" or game[0] == "B" and game[1] == "Y" or game[0] == "C" and game[1] == "Z":
		# Draw
		match game[1]:
			case "X":
				result += rock + draw
			case "Y":
				result += paper + draw
			case "Z":
				result += scissors + draw

	if game[0] == "A" and game[1] == "Z" or game[0] == "B" and game[1] == "X" or game[0] == "C" and game[1] == "Y":
		# Lose
		match game[1]:
			case "X":
				result += rock + lose
			case "Y":
				result += paper + lose
			case "Z":
				result += scissors + lose

print(f"Part {1}:{result}")

result = 0
"""
A = Rock
B = Paper
C = Scissors
"""
for game in data:
	if game[1] == "Z":
		# Win
		match game[0]:
			case "A":
				result += paper + win
			case "B":
				result += scissors + win
			case "C":
				result += rock + win
	if game[1] == "Y":
		# Draw
		match game[0]:
			case "A":
				result += rock + draw
			case "B":
				result += paper + draw
			case "C":
				result += scissors + draw
	if game[1] == "X":
		# Lose
		match game[0]:
			case "A":
				result += scissors + lose
			case "B":
				result += rock + lose
			case "C":
				result += paper + lose

print(f"Part {2}:{result}")
