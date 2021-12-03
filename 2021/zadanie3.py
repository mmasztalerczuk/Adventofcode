import sys

data = []
for l in sys.stdin.readlines():
    data.append(l[:-1])
    
def foo(data):
    c=0
    p = [0,0,0,0,0,0,0,0,0,0,0,0]
    for l in data:
        for i, v in enumerate(l):
            p[i]+=int(v)
        c+=1 
    o = ["1" if x > c/2 else "0" for x in p]
    i = ["0" if x > c/2 else "1" for x in p]

    val1 = "".join(o)
    val2 = "".join(i)

    val1=int(val1, 2)
    val2=int(val2, 2)
    return val1*val2

def check_common_bit_on_position(data, position):
    c=0
    p = [0,0,0,0,0,0,0,0,0,0,0,0]
    for l in data:
        for i, v in enumerate(l):
            p[i]+=int(v)
        c+=1 
    o = ["1" if x >= c/2 else "0" for x in p]
    i = ["0" if x >= c/2 else "1" for x in p]

    return o[position], i[position]

def filter_data(data, position, bit):
    tmp = []
    for l in data:
        if l[position] == bit:
            tmp.append(l)
    return tmp

p = 0
org = data
while len(data) > 1:
    print(data)
    mo, le = check_common_bit_on_position(data, p)
    data = filter_data(data, p, mo)
    p+=1
val1 = "".join(data)    
val1=int(val1, 2)
data=org
p = 0

while len(data) > 1:
    print(data)
    mo, le = check_common_bit_on_position(data, p)
    data = filter_data(data, p, le)
    p+=1
val2 = "".join(data)    
val2=int(val2, 2)
print(val1* val2)

