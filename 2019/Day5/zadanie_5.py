import sys
n = input().split(',')
print(n)
n = list(map(int, n))
i = 0
while True:
#print(i)
    if n[i] == 99:
        break
    val = str(n[i])
    val = "0"*(5-len(val)) + val
    #print(i)
    #print(val)
    if val[-2:] == "01":

        if val[-3] == '1':
            p1 = n[i+1]
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        else:
            p2 = n[n[i+2]]

        n[n[i+3]] = p1 + p2
        i+=3
    elif val[-2:] == "02":
        if val[-3] == '1':
            p1 = n[i+1]
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        else:
            p2 = n[n[i+2]]

        n[n[i+3]] = p1 * p2
        i+=3
    elif val[-2:] == "03":
        n[n[i+1]] = int(input())
        i+=1
    elif val[-2:] == "04":
        if val[-3] == '1':
            p1 = n[i+1]
        else:
            p1 = n[n[i+1]]
        print(p1)
        i+=1
    elif val[-2:] == "05":
        if val[-3] == '1':
            p1 = n[i+1]
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        else:
            p2 = n[n[i+2]]
        if p1 != 0:
            i = p2-1
        else:
            i+=2
    elif val[-2:] == "06":
        if val[-3] == '1':
            p1 = n[i+1]
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        else:
            p2 = n[n[i+2]]
        if p1 == 0:
            i = p2-1
        else:
            i+=2
    elif val[-2:] == "07":
        if val[-3] == '1':
            p1 = n[i+1]
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        else:
            p2 = n[n[i+2]]

        if p1 < p2:
            n[n[i+3]] = 1
        else:
            n[n[i+3]] = 0
        
        i+=3
    elif val[-2:] == "08":
        if val[-3] == '1':
            p1 = n[i+1]
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        else:
            p2 = n[n[i+2]]

        if p1 == p2:
            n[n[i+3]] = 1
        else:
            n[n[i+3]] = 0
        
        i+=3        
    else:
        print("error")
        sys.exit(-1)
    i += 1
#print(n)

