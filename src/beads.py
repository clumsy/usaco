"""
ID: alex.zh6
LANG: PYTHON3
TASK: beads
"""

fin = open("beads.in", "r")
input = lambda: fin.readline().rstrip()
n, s = int(input()), input()

# Solution 1
# lbs, lrs = [0] * n, [0] * n
# lb = lr = 0
# for i in range(2 * n):
#     i %= n
#     lb = min(n, lb + 1) if s[i] in "bw" else 0
#     lr = min(n, lr + 1) if s[i] in "rw" else 0
#     lbs[i], lrs[i] = lb, lr
# rbs, rrs = [0] * n, [0] * n
# rb = rr = 0
# for i in range(2 * n - 1, 0, -1):
#     i %= n
#     rb = min(n, rb + 1) if s[i] in "bw" else 0
#     rr = min(n, rr + 1) if s[i] in "rw" else 0
#     rbs[i], rrs[i] = rb, rr
# res = 0
# for i in range(n):
#     res = min(n, max(res, lbs[i] + rrs[(i + 1) % n], lrs[i] + rbs[(i + 1) % n]))

# Solution 2
s = s + s  # Double the string to handle circularity
cur_clr = None
cur_len = prv_len = trl_wht = res = 0
for c in s:
    if c == "w":
        cur_len += 1
        trl_wht += 1
    elif cur_clr is None or c == cur_clr:
        cur_clr = c
        cur_len += 1
        trl_wht = 0
    else:
        res = max(res, prv_len + cur_len)
        prv_len = cur_len - trl_wht
        cur_len = trl_wht + 1
        trl_wht = 0
        cur_clr = c
    if res >= n:
        res = n
        break
res = min(n, max(res, prv_len + cur_len))

with open("beads.out", "w") as fout:
    print(res, file=fout)
