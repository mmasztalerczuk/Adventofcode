import sys
import itertools
import copy
n = input().split(',')
n = list(map(int, n))
org_n = copy.copy(n)
print(n)


tmp = [5, 6, 7, 8, 9]
order_seq = itertools.permutations(tmp)
ans = 0
prev = 0
for seq in order_seq:
    ans = max(ans, prev)
    print("ans", ans, prev)
    w = 0
    prev = 0
    i = 0
    input_q = 0
    n = copy.copy(org_n)

    print(seq)
    memory = [copy.copy(org_n), copy.copy(org_n), copy.copy(org_n), copy.copy(org_n), copy.copy(org_n)]
    memory_pointer = [0, 0, 0, 0, 0]
    ini = [0, 0, 0, 0, 0]
    acc = 0
    while True:
        n = memory[acc]
        if n[i] == 99:
            #print("break")
            break
        val = str(n[i])
        val = "0"*(5-len(val)) + val
        #print(n)
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
            if ini[acc] == 0:
                n[n[i+1]] = seq[w]
                print('load', seq[w])
                w += 1
                w = w%5
                input_q = 1
                ini[acc] = 1
            else:
                n[n[i+1]] = prev
                print('prev', prev)

            i+=1
        elif val[-2:] == "04":
            if val[-3] == '1':
                p1 = n[i+1]
            else:
                p1 = n[n[i+1]]
            prev = p1
            memory_pointer[acc] = i+2

            acc += 1
            acc = acc%5
            i=memory_pointer[acc]-2
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
        #print("end")
ans = max(ans, prev)
print(ans)

