ans = 0
for i in range(206938, 679129):
    p = str(i)
    c = True
    w = False
    for j in range(1,6):
        if p[j]<p[j-1]:
            c=False
        if p[j]==p[j-1]:
            w = True
    if not w:
        c = False
    if c:
        ans += 1
print(ans)