"""
ID: alex.zh6
LANG: PYTHON3
TASK: crypt1
"""


def only_has(x, a, n):
    if x > n:
        return False
    while x:
        x, r = divmod(x, 10)
        if r not in a:
            return False
    return True


fin = open("crypt1.in", "r")
input = lambda: fin.readline().rstrip()
n, a = int(input()), (int(i) for i in input().split())
a, res = set(a), 0
for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                x = i1 * 100 + i2 * 10 + i3
                if only_has(x * i4, a, 999):
                    for i5 in a:
                        res += only_has(x * i5, a, 999) and only_has(x * (i4 * 10 + i5), a, 9999)
with open("crypt1.out", "w") as fout:
    print(res, file=fout)
