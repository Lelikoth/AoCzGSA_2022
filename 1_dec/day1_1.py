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

print(max(elf_carry))