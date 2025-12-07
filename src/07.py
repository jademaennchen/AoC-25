#AoC-25_07

grid = [l.strip() for l in open('input/07.txt').readlines()]
beams = {x: 0 if grid[0][x] == '.' else 1 for x in range(len(grid[0]))}
p1 = 0

for y in range(1, len(grid)):
    for x, size in beams.items():
        if size == 0 or grid[y][x] == '.': continue
        p1 += 1
        beams[x-1], beams[x], beams[x+1] = beams[x-1] + size, 0, beams[x+1] + size
p2 = sum([beams[x] for x in beams])

print(p1), print(p2)
