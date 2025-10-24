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
trie = {}
for d in dct:
    cur = trie
    for c in d:
        nxt = cur.get(c, {})
        if not nxt:
            nxt = cur[c] = {}
        cur = nxt
    cur["_term_"] = True
fin = open("namenum.in", "r")
input = lambda: fin.readline().rstrip()
s = input()
nxts = [(trie, "")]
for c in s:
    curs, nxts = nxts, []
    for cur, val in curs:
        for k in m[c]:
            if k in cur:
                nxts.append((cur[k], val + k))
nxts = [v for n, v in nxts if "_term_" in n]
res = sorted(nxts) if nxts else ["NONE"]
with open("namenum.out", "w") as fout:
    print(*res, sep="\n", file=fout)
