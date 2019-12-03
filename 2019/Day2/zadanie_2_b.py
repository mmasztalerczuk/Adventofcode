import copy
org = input().split(',')
org = list(map(int, org))

for w in range(10000):
    #print(w)
    for j in range(10000):
        #print(w, j)
        n = copy.copy(org)
        i = 0
        n[1] = w
        n[2] = j
        while True:
            try:
                if n[i] == 99:
                    break
                if n[i] == 1:
                    n[n[i+3]] = n[n[i+1]] + n[n[i+2]]
                    i+=3
                elif n[i] == 2:
                    n[n[i+3]] = n[n[i+1]] * n[n[i+2]]
                    i+=3
            except IndexError:
                break   
            i += 1
        if n[0] == 19690720:
            print('wynik', w, j)

