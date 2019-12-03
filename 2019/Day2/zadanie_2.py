n = input().split(',')
print(n)
n = list(map(int, n))
i = 0
n[1] = 12
n[2] = 2
while True:
    if n[i] == 99:
        break
    if n[i] == 1:
        n[n[i+3]] = n[n[i+1]] + n[n[i+2]]
        i+=3
    elif n[i] == 2:
        n[n[i+3]] = n[n[i+1]] * n[n[i+2]]
        i+=3
    i += 1
print(n)

