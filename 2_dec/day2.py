

with open("2_dec/input.txt") as f:
    lines = f.readlines()

play = {"Rock": ["A","X"], "Paper": ["B","Y"], "Scissors": ["C","Z"]}

lines = [line.strip() for line in lines]


# Part 1
score = 0

for line in lines:
    line = line.strip().split(" ")
    if line[0] in play["Rock"] and line[1] in play["Paper"]:
        score += 8
    elif line[0] in play["Paper"] and line[1] in play["Scissors"]:
        score += 9
    elif line[0] in play["Scissors"] and line[1] in play["Rock"]:
        score += 7
    elif line[0] in play["Rock"] and line[1] in play["Scissors"]:
        score += 3
    elif line[0] in play["Paper"] and line[1] in play["Rock"]:
        score += 1
    elif line[0] in play["Scissors"] and line[1] in play["Paper"]:
        score += 2
    elif line[0] and line[1] in play["Rock"]:
        score += 4
    elif line[0] and line[1] in play["Paper"]:
        score += 5
    elif line[0] and line[1] in play["Scissors"]:
        score += 6

print(score)


#part 2
score2 = 0

for line in lines:
    line = line.strip().split(" ")
    if line[0] in play["Rock"]:
        if line[1] == "X":
            score2 += 3
        elif line[1] == "Y":
            score2 += 4
        elif line[1] == "Z":
            score2 += 8
    elif line[0] in play["Paper"]:
        if line[1] == "X":
            score2 += 1
        elif line[1] == "Y":
            score2 += 5
        elif line[1] == "Z":
            score2 += 9
    elif line[0] in play["Scissors"]:
        if line[1] == "X":
            score2 += 2
        elif line[1] == "Y":
            score2 += 6
        elif line[1] == "Z":
            score2 += 7


print(score2)