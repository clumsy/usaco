"""
ID: alex.zh6
LANG: PYTHON3
TASK: palsquare
"""


def ispal(s):
    b, e = 0, len(s) - 1
    while b < e:
        if s[b] != s[e]:
            return False
        b += 1
        e -= 1
    return True


def inb(n, b):
    res = []
    while n:
        n, r = divmod(n, b)
        res.append(str(r) if r < 10 else chr(ord("A") + r - 10))
    return "".join(res[::-1])


fin = open("palsquare.in", "r")
input = lambda: fin.readline().rstrip()
b = int(input())
res = (f"{inb(n, b)} {inb(n * n, b)}" for n in range(1, 301) if ispal(inb(n * n, b)))
with open("palsquare.out", "w") as fout:
    print(*res, sep="\n", file=fout)
