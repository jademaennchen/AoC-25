#AoC-25_08

import math as m

coords = [list(map(int, l.strip().split(','))) for l in open('input/08.txt').readlines()]
distances = [((i, j), m.sqrt(sum([(coords[i][k]-coords[j][k])**2 for k in range(3)]))) for i in range(len(coords)) for j in range(i+1, len(coords))]
circuits, roots = [[i] for i in range(len(coords))], {i: i for i in range(len(coords))}

for i, ((c1, c2), dist) in enumerate(sorted(distances, key = lambda x: x[1])):
    if i == 1000: p1 = m.prod(len(c) for c in sorted(circuits, key = len)[-3:])
    if roots[c1] == roots[c2]: continue
    circuits[roots[c1]] =  circuits[roots[c1]] + circuits[roots[c2]]
    origin = roots[c2]
    for c in circuits[origin]: roots[c] = roots[c1]
    circuits[origin] = []
    if len(circuits[roots[c1]]) == len(coords): p2 = coords[c1][0] * coords[c2][0]

print(p1, p2)
