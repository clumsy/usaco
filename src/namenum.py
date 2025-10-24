"""
ID: alex.zh6
LANG: PYTHON3
TASK: namenum
"""

m = {
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PRS",
    "8": "TUV",
    "9": "WXY",
}
dct = (l.rstrip() for l in open("dict.txt", "r"))
fin = open("namenum.in", "r")
input = lambda: fin.readline().rstrip()
s = input()

# Solution1
# trie = {}
# for d in dct:
#     cur = trie
#     for c in d:
#         nxt = cur.get(c, {})
#         if not nxt:
#             nxt = cur[c] = {}
#         cur = nxt
#     cur["_term_"] = True
# nxts = [(trie, "")]
# for c in s:
#     curs, nxts = nxts, []
#     for cur, val in curs:
#         for k in m[c]:
#             if k in cur:
#                 nxts.append((cur[k], val + k))
# nxts = [v for n, v in nxts if "_term_" in n]

# Solution 2
s = int(s)
rm = dict((c, int(k)) for k, v in m.items() for c in v)


def convert(d):
    r = 0
    for c in d:
        if c not in rm:
            return -1
        r = r * 10 + rm[c]
    return r


nxts = [d for d in dct if convert(d) == s]
res = sorted(nxts) if nxts else ["NONE"]
with open("namenum.out", "w") as fout:
    print(*res, sep="\n", file=fout)
