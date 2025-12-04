#AoC-25_04

grid = [l.strip() for l in open('input/04.txt').readlines()]
rolls = [(y, x) for y in range(len(grid)) for x in range(len(grid)) if grid[y][x] == '@']
adjacent = {(y, x): sum([(y+dy, x+dx) in rolls for dy in (-1, 0, 1) for dx in (-1, 0, 1)]) for y, x in rolls}
done, p2 = False, 0

p1 = sum([adjacent[y, x] < 5 for y, x in adjacent])

while(not done):
    removable, done = set(), True
    for y, x in adjacent:
        if adjacent[y, x] < 5:
            p2, done = p2 + 1, False
            removable.add((y, x))
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if (y+dy, x+dx) in adjacent: adjacent[y+dy, x+dx] -= 1
    for y, x in removable: adjacent.pop((y, x))

print(p1), print(p2)
