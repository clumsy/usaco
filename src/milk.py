"""
ID: alex.zh6
LANG: PYTHON3
TASK: milk
"""

from heapq import heappush, heappop


fin = open("milk.in", "r")
input = lambda: fin.readline().rstrip()
n, m = (int(i) for i in input().split())
h = []
for _ in range(m):
    p, a = (int(i) for i in input().split())
    heappush(h, (p, a))
res = 0
while n:
    p, a = heappop(h)
    d = min(n, a)
    res += d * p
    n -= d
with open("milk.out", "w") as fout:
    print(res, file=fout)
