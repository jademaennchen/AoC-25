#AoC-25_05

ranges = sorted([list(map(int, l.strip().split('-'))) for l in open('input/05.txt').readlines() if l.count('-') > 0], key = lambda x: x[0])
ids = [int(l.strip()) for l in open('input/05.txt').readlines() if l.strip().isnumeric()]
cut_ranges = ranges[:1]

p1 = sum(any(start <= id <= end for start, end in ranges) for id in ids)

for start, end in ranges:
    if end <= cut_ranges[-1][1]: continue
    if start <= cut_ranges[-1][1]:
        cut_ranges[-1][1] = end
        continue
    cut_ranges.append([start, end])
p2 = sum([end-start+1 for start, end in cut_ranges])

print(p1), print(p2)
