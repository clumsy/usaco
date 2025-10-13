"""
ID: alex.zh6
LANG: PYTHON3
TASK: ride
"""

from operator import mul
from functools import reduce


fin = open("ride.in", "r")
input = lambda: fin.readline().rstrip()
c, g = (input() for _ in range(2))
res = (
    "GO"
    if reduce(mul, (ord(i) - ord("A") + 1 for i in c)) % 47 == reduce(mul, (ord(i) - ord("A") + 1 for i in g)) % 47
    else "STAY"
)
with open("ride.out", "w") as fout:
    print(res, file=fout)
