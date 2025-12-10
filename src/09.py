#AoC-25_09

coords = [tuple(map(int, l.strip().split(','))) for l in open('input/09.txt').readlines()]
pairs = sorted([((c1, c2), (abs(c2[0]-c1[0])+1)*(abs(c2[1]-c1[1])+1))  for i, c1 in enumerate(coords) for c2 in coords[i+1:]], key = lambda x: x[1], reverse = True)

for ((x1, y1), (x2, y2)), area in pairs:
    px, py = 1 if x2 >= x1 else -1, 1 if y2 >= y1 else -1
    if not any(((x2-x3) * -px >= 0) and ((y1-y3) * py >= 0) for x3, y3 in coords): continue
    if not any(((x1-x3) * px >= 0) and ((y2-y3) * -py >= 0) for x3, y3 in coords): continue
    for i, (x3, y3) in enumerate(coords):
        x4, y4 = coords[i-1]
        if min(x1, x2) < x3 < max(x1, x2) and min(y1, y2) < y3 < max(y1, y2): break
        if min(x1, x2) < x3 == x4 < max(x1, x2) and min(y3, y4) <= min(y1, y2) and max(y1, y2) <= max(y3, y4): break
        if min(y1, y2) < y3 == y4 < max(y1, y2) and min(x3, x4) <= min(x1, x2) and max(x1, x2) <= max(x3, x4): break
    else:
        p1, p2 = pairs[0][1], area
        break

print(p1, p2)
