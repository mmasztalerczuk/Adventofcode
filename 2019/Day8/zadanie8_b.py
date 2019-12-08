w = 25
t = 6
n = input()
m = w*t
l_len = len(n)//(w*t)
layers = []
for i in range(l_len):
    layers.append([])
print(l_len)
p = 0
for i in n:
    layers[p//m].append(i)
    p += 1

final_layer = []
for i in range(150):
    tmp = 0
    while True:
        if layers[tmp][i] == '2':
            tmp += 1
        else:
            final_layer.append(layers[tmp][i])
            break
p = 0
for i in final_layer:
    if p%25==0:
        print()
    if i == '1':
        print(i, end="")
    else:
        print(' ', end="")
    p+=1
