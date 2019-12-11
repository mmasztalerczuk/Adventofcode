import sys
n = input().split(',')
print(n)
n = list(map(int, n))
for i in range(100000):
    n.append(0)
i = 0
relative_base = 0
d = {}
x = 0
y = 0
f = 0
deg = 90
d[(0,0)]=1
while True:
#print(i)
    if n[i] == 99:
        break
    val = str(n[i])
    val = "0"*(5-len(val)) + val
    #print(i)
    #print(val, ' ', end="")
    if val[-2:] == "01":

        if val[-3] == '1':
            p1 = n[i+1]
        elif val[-3] == '2':
            p1 = n[relative_base + n[i+1]]           
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        elif val[-4] == '2':
            p2 = n[relative_base + n[i+2]]                  
        else:
            p2 = n[n[i+2]]

        if val[-5] == '1':
            p3 = i+3
        elif val[-5] == '2':
            p3 = relative_base + n[i+3]        
        else:
            p3 = n[i+3]            

            
        #print('add', p1, p2, 'to', n[i+3], 'cell')
        n[p3] = p1 + p2
        i+=3
    elif val[-2:] == "02":
        if val[-3] == '1':
            p1 = n[i+1]
        elif val[-3] == '2':
            p1 = n[relative_base + n[i+1]]             
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        elif val[-4] == '2':
            p2 = n[relative_base + n[i+2]]              
        else:
            p2 = n[n[i+2]]

        if val[-5] == '1':
            p3 = i+3
        elif val[-5] == '2':
            p3 = relative_base + n[i+3]        
        else:
            p3 = n[i+3]            

        n[p3] = p1 * p2
        i+=3
    elif val[-2:] == "03":
        if val[-3] == '1':
            p1 = i+1
        elif val[-3] == '2':
            p1 = relative_base + n[i+1]           
        else:
            p1 = n[i+1]
        if (x,y) in d:
            n[p1] = d[(x,y)]
        else:
            d[(x,y)] = 0
            n[p1] = 0
        i+=1
    elif val[-2:] == "04":
        if val[-3] == '1':
            p1 = n[i+1]
        elif val[-3] == '2':
            p1 = n[relative_base + n[i+1]]
        else:
            p1 = n[n[i+1]]
        if f == 0:
            d[(x, y)] = p1
            f = 1
        elif f == 1:
            if p1 == 0:
                deg += 90
            else:
                deg -= 90
            f = 0

            if deg < 0:
                deg = 270
            if deg > 270:
                deg = 0

            if deg == 90:
                y += 1
            if deg == 180:
                x -= 1
            if deg == 270:
                y -= 1
            if deg == 0:
                x += 1
#            print(len(d))
        i+=1
    elif val[-2:] == "05":
        if val[-3] == '1':
            p1 = n[i+1]
        elif val[-3] == '2':
            p1 = n[relative_base + n[i+1]]              
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        elif val[-4] == '2':
            p2 = n[relative_base + n[i+2]]             
        else:
            p2 = n[n[i+2]]
        if p1 != 0:
            i = p2-1
        else:
            i+=2
    elif val[-2:] == "06":
        if val[-3] == '1':
            p1 = n[i+1]
        elif val[-3] == '2':
            p1 = n[relative_base + n[i+1]]             
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        elif val[-4] == '2':
            p2 = n[relative_base + n[i+2]]              
        else:
            p2 = n[n[i+2]]

        if p1 == 0:
            i = p2-1
            #print("jump", p2, n[i+2])
        else:
            i+=2
    elif val[-2:] == "07":
        if val[-3] == '1':
            p1 = n[i+1]
        elif val[-3] == '2':
            p1 = n[relative_base + n[i+1]]            
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        elif val[-4] == '2':
            p2 = n[relative_base + n[i+2]]             
        else:
            p2 = n[n[i+2]]

        if val[-5] == '1':
            p3 = i+3
        elif val[-5] == '2':
            p3 = relative_base + n[i+3]        
        else:
            p3 = n[i+3]

        if p1 < p2:
            n[p3] = 1
        else:
            n[p3] = 0
        
        i+=3
    elif val[-2:] == "08":
        if val[-3] == '1':
            p1 = n[i+1]
        elif val[-3] == '2':
            p1 = n[relative_base + n[i+1]]             
        else:
            p1 = n[n[i+1]]

        if val[-4] == '1':
            p2 = n[i+2]
        elif val[-4] == '2':
            p2 = n[relative_base + n[i+2]]             
        else:
            p2 = n[n[i+2]]
        #print('compare', p1, p2, 'set', p1==p2, 'to', n[i+3], 'cell')
        if val[-5] == '1':
            p3 = i+3
        elif val[-5] == '2':
            p3 = relative_base + n[i+3]        
        else:
            p3 = n[i+3]

        if p1 == p2:
            n[p3] = 1
        else:
            n[p3] = 0
        i+=3
    elif val[-2:] == "09":
        if val[-3] == '1':
            p1 = n[i+1]
        elif val[-3] == '2':
            p1 = n[relative_base + n[i+1]]            
        else:
            p1 = n[n[i+1]]  
        relative_base += p1
        #print('set relative_base', relative_base)
        i+=1              
    else:
        print("error", val)
        sys.exit(-1)
    i += 1
#print(n)
print(len(d))
print(d)
for q in range(-20,200):
    for w in range(-20, 200):
        if (q,w) in d and d[(q,w)]==1:
            print('#', end="")
        else:
            print('.', end="")
    print()
