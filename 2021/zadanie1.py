import sys
p = None
a = 0

data_val = []

def calculate_inc(data):
    a = 0
    p = None
    for d in data:
        v = d
        if p is None:
            p = v
        else:
            if v-p > 0:
                a += 1
            p = v
    return a

def sum_three_measurement(data):
    l = []
    a, b, c = data[0], data[1], data[2]
    for d in data[2:]:
        l.append(a+b+c)
        a,b,c=b,c,d
    return l


for l in sys.stdin.readlines():
    data_val.append(int(l[:-1]))

print(calculate_inc(sum_three_measurement(data_val)))
