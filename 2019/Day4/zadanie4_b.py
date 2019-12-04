ans = 0
for i in range(206938, 679129):
    p = str(i)
    c = True
    w = False
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(1,6):          
        if p[j]<p[j-1]:
            c=False
        if p[j]==p[j-1]:
            if l[int(p[j])] == 0:
                l[int(p[j])] = 1
            elif l[int(p[j])] == 1:
                l[int(p[j])] = 2           
    for j in l:
        if j == 1:
            w = True
    if not w:
        c = False
    if c:
        ans += 1
print(ans)