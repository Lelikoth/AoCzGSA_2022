
from collections import defaultdict

with open('7_dec/input.txt') as f:
    files = defaultdict(list)
    parent = {}
    path = []
    root = ''

    for line in f.readlines():
        parts = line.strip().split(' ')
        current_dir = ''.join(path)

        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '..':
                    path.pop()
                elif parts[2] == '/':
                    parent[''] = 'tmp'
                    path.append('')
                else:
                    parent[current_dir + '/' + parts[2]] = current_dir
                    path.append('/' + parts[2])
        else:
            if parts[0] == 'dir':
                parent[current_dir + '/' + parts[1]] = current_dir
            else:
                files[current_dir].append((int(parts[0]), parts[1]))

    next_to = defaultdict(set)
    for directory in parent:
        if parent[directory] != 'tmp':
            next_to[parent[directory]].add(directory)


# Part 1

def sum1(next_to, files):
    result = 0

    def search(root):
        current_total = 0
        for neighbour in next_to[root]:
            current_total += search(neighbour)

        for size, _ in files[root]:
            current_total += size

        if current_total <= 100_000:
            nonlocal result
            result += current_total

        return current_total

    search(root)
    print(result)


sum1(next_to, files)


# Part 2

def sum2(next_to, files):
    lookup = {}

    def search(root):
        current_total = 0
        for neighbour in next_to[root]:
            current_total += search(neighbour)

        for size, _ in files[root]:
            current_total += size

        lookup[root] = current_total
        return current_total

    search(root)

    print(min(value for value in lookup.values() if value >=
          30_000_000 - (70_000_000 - lookup[root])))


sum2(next_to, files)
