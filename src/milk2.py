"""
ID: alex.zh6
LANG: PYTHON3
TASK: milk2
"""

fin = open("milk2.in", "r")
input = lambda: fin.readline().rstrip()
n = int(input())
m = sorted(([int(i) for i in input().split()] for _ in range(n)), key=lambda x: x[0])
some = none = 0
start, end = m[0]
for b, e in m[1:]:
    if b <= end:
        end = max(end, e)
    else:
        some = max(some, end - start)
        none = max(none, b - end)
        start, end = b, e
some = max(some, end - start)
res = some, none
with open("milk2.out", "w") as fout:
    print(*res, file=fout)
