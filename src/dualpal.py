"""
ID: alex.zh6
LANG: PYTHON3
TASK: dualpal
"""


def ispal(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        if a[lo] != a[hi]:
            return False
        lo += 1
        hi -= 1
    return True


def inbase(n, b):
    res = []
    while n:
        n, r = divmod(n, b)
        res.append(r)
    return res[::-1]


fin = open("dualpal.in", "r")
input = lambda: fin.readline().rstrip()
n, s = (int(i) for i in input().split())
res = []
while len(res) < n:
    s += 1
    cnt = 0
    for b in range(2, 11):
        if ispal(inbase(s, b)):
            cnt += 1
            if cnt > 1:
                res.append(s)
                break
with open("dualpal.out", "w") as fout:
    print(*res, sep="\n", file=fout)
