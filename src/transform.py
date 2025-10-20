"""
ID: alex.zh6
LANG: PYTHON3
TASK: transform
"""


def same(bfr, afr):
    return all(a == b for a, b in zip(bfr, afr))


def ref(bfr, afr):
    return same([s[::-1] for s in bfr], afr)


def rot(bfr, afr):
    n = len(bfr)
    if all(bfr[r][c] == afr[c][n - 1 - r] for r in range(n) for c in range(n)):
        return 1
    if same([s[::-1] for s in bfr[::-1]], afr):
        return 2
    if all(bfr[r][c] == afr[n - 1 - c][r] for r in range(n) for c in range(n)):
        return 3
    return None


def comb(bfr, afr):
    return rot([s[::-1] for s in bfr], afr)


fin = open("transform.in", "r")
input = lambda: fin.readline().rstrip()
n = int(input())
bfr = [input() for _ in range(n)]
afr = [input() for _ in range(n)]
if r := rot(bfr, afr):
    res = r
elif ref(bfr, afr):
    res = 4
elif comb(bfr, afr):
    res = 5
elif same(bfr, afr):
    res = 6
else:
    res = 7
with open("transform.out", "w") as fout:
    print(res, file=fout)
