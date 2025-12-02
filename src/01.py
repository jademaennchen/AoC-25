#AoC-25_01

rotations = [(l[0], int(l[1:])) for l in open('input/01.txt').readlines()]
total, p1, p2 = 50, 0, 0

for dir, step in rotations:
    prev = total
    total += step if dir == 'R' else -step
    if total % 100 == 0: p1 += 1
    if prev % 100 == 0: p2 -= 1
    p2 += max(total, prev) // 100 - min(total-1, prev-1) // 100

print(p1), print(p2)
