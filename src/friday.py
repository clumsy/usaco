"""
ID: alex.zh6
LANG: PYTHON3
TASK: friday
"""

fin = open("friday.in", "r")
input = lambda: fin.readline().rstrip()
ds = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n, d = int(input()), 0
res = [0] * 7
for y in range(n):
    y += 1900
    for m in range(12):
        res[(d + 12) % 7] += 1
        l = 1 if m == 1 and y % 4 == 0 and (y % 400 == 0 or y % 100 != 0) else 0
        d = (d + ds[m] + l) % 7
res = res[-2:] + res[:-2]
with open("friday.out", "w") as fout:
    print(*res, file=fout)
