#AoC-25_11

devices = {l[:3]: l[5:].strip().split() for l in open('input/11.txt').readlines()}
paths = {'out': [1, 0, 0]}
p1, p2 = 0, 0

def visit(cur):
    if not cur in paths:
        total = [sum(count) for count in zip(*[visit(next) for next in devices[cur]])]
        if cur == 'dac': total[1] = total[0]
        if cur == 'fft': total[2] = total[1]
        paths[cur] = total
    return paths[cur]
p1, p2 = visit('you')[0], visit('svr')[2]

print(p1, p2)
