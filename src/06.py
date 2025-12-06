#AoC-25_06

import math as m

data = [l[:-1] for l in open('input/06.txt').readlines()[:-1]]
operations = open('input/06.txt').readlines()[-1].strip().split()
spaces = [-1] + [i for i in range(len(data[0])) if all(data[j][i] == ' ' for j in range(len(data)))] + [len(data[0])]
p1, p2 = 0, 0

for i, op in enumerate(operations):
    nums = [data[j][spaces[i]+1:spaces[i+1]] for j in range(len(data))]
    inv_nums = [''.join([nums[j][k] for j in range(len(data))]) for k in range(len(nums[0]))]
    if op == '+':
        p1 += sum([int(nums[j]) for j in range(len(data))])
        p2 += sum([int(inv_nums[j]) for j in range(len(inv_nums))])
    else:
        p1 += m.prod([int(nums[j]) for j in range(len(data))])
        p2 += m.prod([int(inv_nums[j]) for j in range(len(inv_nums))])

print(p1), print(p2)
