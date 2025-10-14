"""
ID: alex.zh6
LANG: PYTHON3
TASK: gift1
"""

from collections import OrderedDict


fin = open("gift1.in", "r")
input = lambda: fin.readline().rstrip()
n = int(input())
res = OrderedDict([(name, 0) for name in (input() for _ in range(n))])
for _ in range(n):
    name = input()
    m, ng = (int(i) for i in input().split())
    p, r = divmod(m, ng) if ng else (0, 0)
    res[name] -= p * ng
    for _ in range(ng):
        res[input()] += p
res = (f"{k} {v}" for k, v in res.items())
with open("gift1.out", "w") as fout:
    print(*res, sep="\n", file=fout)
