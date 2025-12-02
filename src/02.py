#AoC-25_02

ranges = [r.split('-') for l in open('input/02.txt').readlines() for r in l.strip().split(',')]
p1, p2 = 0, set()

def is_invalid(start, end, num, factor):
    if int(start) <= int(factor*num) <= int(end) and factor > 1: return int(factor*num)
    return 0

for start, end in ranges:
    for num in [str(i) for i in range(1, pow(10, len(end)//2))]:
        p2.add(is_invalid(start, end, num, len(start)//len(num)))
        p2.add(is_invalid(start, end, num, len(end)//len(num)))
        p1 += is_invalid(start, end, num, 2)

print(p1), print(sum(p2))
