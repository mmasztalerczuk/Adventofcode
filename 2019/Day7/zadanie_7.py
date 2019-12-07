import sys
import itertools
n = input().split(',')
print(n)


tmp = [0, 1, 2, 3, 4]
order_seq = itertools.permutations(tmp)
ans = 0
prev = 0
for seq in order_seq:
    ans = max(ans, prev)
    prev = 0
    print()
    for seq_i in range(5):
        print(seq[seq_i], prev)
        n = list(map(int, n))
        i = 0
        input_q = 0
        while True:
            if n[i] == 99:
                break
            val = str(n[i])
            val = "0"*(5-len(val)) + val
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
                if input_q == 0:
                    n[n[i+1]] = seq[seq_i]
                    input_q = 1
                else:
                    n[n[i+1]] = prev
                i+=1
            elif val[-2:] == "04":
                if val[-3] == '1':
                    p1 = n[i+1]
                else:
                    p1 = n[n[i+1]]
                #print(p1)
                prev = p1
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
ans = max(ans, prev)
print(ans)

