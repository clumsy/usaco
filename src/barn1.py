"""
ID: alex.zh6
LANG: PYTHON3
TASK: barn1
"""

from heapq import heappop, heappush


fin = open("barn1.in", "r")
input = lambda: fin.readline().rstrip()
m, s, c = (int(i) for i in input().split())
cs = (int(input()) for _ in range(c))
b, e, p = s, 0, None
res, h = c, []
for c in sorted(cs):
    p = p or (c - 1)
    b = min(b, c)
    e = max(e, c)
    g = c - p - 1
    if g:
        heappush(h, -g)
    p = c
while h and m - 1 > 0:
    heappop(h)
    m -= 1
res += -sum(h)
with open("barn1.out", "w") as fout:
    print(res, file=fout)
