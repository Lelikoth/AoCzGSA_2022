

with open('6_dec/input.txt') as f:
    lines = f.read().splitlines()


lines = [line.strip() for line in lines]

# Part 1

def find_seq(lines):
    for line in lines:
        for i in range(len(line)-3):
            if len(set(line[i:i+4])) == 4:
                return i+3


print(find_seq(lines)+1)


# Part 2

def find_seq2(lines):
    for line in lines:
        for i in range(len(line)-13):
            if len(set(line[i:i+14])) == 14:
                return i+13

print(find_seq2(lines)+1)