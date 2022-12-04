
with open('4_dec/input.txt', 'r') as f:
    lines = f.readlines()

count = 0
# Part 1
for line in lines:
    line = line.replace("\n" ,"")
    first, second = line.split(",")
    f1 , f2 = first.split("-")
    s1 , s2 = second.split("-")
    f = set()
    s = set()
    for i in range(int(f1), int(f2)+1):
        f.add(i)
    for i in range(int(s1), int(s2)+1):
        s.add(i)
    if f.intersection(s) == f or f.intersection(s) == s:
        count += 1

print(count)

# Part 2
count = 0

for line in lines:
    line = line.replace("\n" ,"")
    first, second = line.split(",")
    f1 , f2 = first.split("-")
    s1 , s2 = second.split("-")
    f = set()
    s = set()
    for i in range(int(f1), int(f2)+1):
        f.add(i)
    for i in range(int(s1), int(s2)+1):
        s.add(i)
    if len(f.intersection(s)) > 0:
        count += 1

print(count)