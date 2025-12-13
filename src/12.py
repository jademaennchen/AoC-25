#AoC-25_12

regions = [[int(l[0:2])*int(l[3:5]), list(map(int, l.strip()[7:].split()))] for l in open('input/12.txt').readlines()[31:]]
sizes = [7, 5, 7, 6, 7, 7]
p1 = 0

for area, pieces in regions:
    if area - sum(pieces[i] * sizes[i] for i in range(6)) > 0: p1 += 1
    print(area, [pieces[i] * sizes[i] for i in range(6)])
    
print(p1)
