import sys
n = []
for l in sys.stdin:
    n.append(l[:-1])
d = {}

def count(w, v, steps):
    print(w, v, steps)
    for o in v:
        if o == 'SAN':
            print("find")
            return steps
    ans = 99999999999999999
    for o in v:
        print(o)
        print(v)
        if vis[o] is False:
            vis[o] = True
            ans = min(ans, count(o, d[o], steps+1))
    return ans
vis = {}

for o in n:
    a, b = o.split(")")
    if not b in d:
        d[b] = []        
    d[b].append(a)
    if not a in d:
        d[a] = []
    d[a].append(b)
    vis[a] = False
    vis[b] = False
#print(d)
#d['YOU'][1] = True
ans = count('YOU', d['YOU'], -1)
print(ans)


