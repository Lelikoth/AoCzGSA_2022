
with open("8_dec/input.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(map(int, line.strip())))


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
length = len(grid)
width = len(grid[0])

# Part 1
visible_trees = 0


for x in range(length):
    for y in range(width):
        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            while(0 <= nx < length and 0 <= ny < width and grid[nx][ny] < grid[x][y]):
                nx += dx
                ny += dy

            if not (0 <= nx < length and 0 <= ny < width):
                visible_trees += 1
                break

# Part 2

best_tree = 0

for x in range(length):
    for y in range(width):
        best = 1
        for dx, dy in directions:
            current_best = 0
            nx, ny = x+dx, y+dy

            while(0 <= nx < length and 0 <= ny < width):
                current_best += 1
                if grid[nx][ny] >= grid[x][y]:
                    break

                nx += dx
                ny += dy

            best *= current_best
        
        best_tree = max(best_tree, best)

print(visible_trees, best_tree)





