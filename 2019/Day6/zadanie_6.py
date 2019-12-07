import sys
n = []
for l in sys.stdin:
    n.append(l[:-1])
d = {}

def count(v):
    print(v)
    ans = len(v)
    for o in v:
        ans += count(d[o])
    return ans


for o in n:
    a, b = o.split(")")
    if not b in d:
        d[b] = []
    d[b].append(a)
    if not a in d:
        d[a] = []

ans = 0
for i in d:
    ans += count(d[i])
print(ans)

