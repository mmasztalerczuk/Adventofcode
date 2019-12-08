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
    print(p, m, p%m)
    layers[p//m].append(i)
    p += 1
print(layers)
ans = 1000
ans_l = []
ans_one = 0
ans_two = 0
for l in layers:
    tmp = 0
    tmp_one = 0
    tmp_two = 0
    print(l)
    for a in l:
        if a == '0':
            tmp += 1
        if a == '1':
            tmp_one += 1
        if a == '2':
            tmp_two += 1
    #print(tmp)
    if tmp < ans:
        ans = tmp
        ans_one = tmp_one
        ans_two = tmp_two
        ans_l = l
print("end")   
print(ans)
print(ans_l)
print(ans_one)
print(ans_two)
print(ans_one*ans_two)
