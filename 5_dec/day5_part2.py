# program to find the final position of the crates

with open('5_dec/input.txt') as f:
    lines = f.readlines()

# create a list of lists
stacks = []

for i in range(9):
    stacks.append([])

# add the crates to the stacks
for j in range(8):
    for i in range(9):
        stacks[i].append(lines[j][i*4 + 1])


#remove all ' ' from the lists
for i in range(9):
    stacks[i] = [x for x in stacks[i] if x != ' ']



#reverse the stacks
for i in range(9):
    stacks[i].reverse()


# move parameters
for line in lines[10:]:
    line = line.split()
    how_many = int(line[1])
    from_stack = int(line[3])-1
    to_stack = int(line[5])-1

    temp = []
    for i in range(how_many):
        if len(stacks[from_stack]) > 0:
            temp.append(stacks[from_stack].pop())
    temp.reverse()
    for i in temp:
        stacks[to_stack].append(i)
            
#get last crate in each stack

for i in range(9):
    print(stacks[i][-1], end='')