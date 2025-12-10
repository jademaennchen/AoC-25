#AoC-25_10

import itertools as it, pulp

data = [l.strip().split() for l in open('input/10.txt').readlines()]
diagrams, joltages = [[1 if c == '#' else 0 for c in list(l[0][1:-1])] for l in data], [list(map(int, l[-1][1:-1].split(','))) for l in data]
buttons, p1, p2 = [[[1 if str(j) in c else 0 for j in range(len(diagrams[i]))] for c in l[1:-1]] for i, l in enumerate(data)], 0, 0

for i in range(len(diagrams)):
    for combination in [list(c) for r in range(1, len(buttons[i])+1) for c in it.combinations(buttons[i], r)]:
        if sum([sum(pos) % 2 != 0 for pos in zip(*(combination + [diagrams[i]]))]) == 0:
            p1 += len(combination)
            break
    solver, x = pulp.LpProblem("get_min", pulp.LpMinimize), [pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer") for j in range(len(buttons[i]))]
    for row in range(len(joltages[i])): solver += sum(x[j] * buttons[i][j][row] for j in range(len(buttons[i]))) == joltages[i][row]
    solver += sum(x)
    solver.solve(pulp.PULP_CBC_CMD(msg=0))
    p2 += int(pulp.value(solver.objective))

print(p1), print(p2)
