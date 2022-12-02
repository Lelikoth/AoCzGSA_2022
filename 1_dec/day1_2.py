elf_inventory = [x for x in open('Advent_of_Code/1_dec/input.txt').read().splitlines()]

elf_carry = []
calories = 0

for x in elf_inventory:
    if x == '':
        elf_carry.append(calories)
        calories = 0
    else:
        calories += int(x)

elf_carry.append(calories)

elf_carry.sort(reverse=True)

print(sum(elf_carry[0:3]))