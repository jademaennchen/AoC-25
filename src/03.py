#AoC-25_03

banks = [list(map(int, l.strip())) for l in open('input/03.txt').readlines()]

def find_max_selection(num):
    ret = 0
    for bank in banks:
        idx = []
        for i in range(num-1, -1, -1):
            start = 0 if i == num-1 else idx[-1]+1
            cur_bank = bank[start:len(bank)-i]
            idx.append(start + cur_bank.index(max(cur_bank)))
        ret += int(''.join([str(bank[i]) for i in idx]))
    return ret

p1, p2 = find_max_selection(2), find_max_selection(12)

print(p1, p2)
