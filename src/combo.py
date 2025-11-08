"""
ID: alex.zh6
LANG: PYTHON3
TASK: combo
"""

from itertools import product


fin = open("combo.in", "r")
input = lambda: fin.readline().rstrip()
n = int(input())
a, b = (tuple(int(i) for i in input().split()) for _ in range(2))

# Solution 1
# cmb = set()
# for x in (a, b):
#     cmb.update(product(*((d % n for d in range(i - 2, i + 3)) for i in x)))
# res = len(cmb)


# Solution 2
def close(x, y):
    return min((x - y) % n, (y - x) % n) <= 2


def close_to(i1, i2, i3, t1, t2, t3):
    return close(i1, t1) and close(i2, t2) and close(i3, t3)


res = 0
for i1 in range(1, n + 1):
    for i2 in range(1, n + 1):
        for i3 in range(1, n + 1):
            if close_to(i1, i2, i3, *a) or close_to(i1, i2, i3, *b):
                res += 1

with open("combo.out", "w") as fout:
    print(res, file=fout)
