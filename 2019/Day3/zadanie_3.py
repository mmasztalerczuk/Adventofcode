d = {}


n1 = input().split(",")
n2 = input().split(",")

start_x = 1000
start_y = 1000
s = 1
for n in n1:
    c = n[0]
    v = int(n[1:])
    for i in range(1,v+1):
        if c == 'R':
            if start_x+1 not in d:
                d[start_x+1] = {}
            d[start_x+1][start_y]=s
            start_x += 1
        if c == 'L':
            if start_x-1 not in d:
                d[start_x-1] = {}            
            d[start_x-1][start_y]=s
            start_x -= 1
        if c == 'U':
            if start_x not in d:
                d[start_x] = {}            
            d[start_x][start_y+1]=s
            start_y += 1
        if c == 'D':
            if start_x not in d:
                d[start_x] = {}
            d[start_x][start_y-1]=s
            start_y -= 1

start_x = 1000
start_y = 1000
min_val = 1000000000000

for n in n2:
    c = n[0]
    v = int(n[1:])

    for i in range(1,v+1):

        if c == 'R':

            if start_x+1 not in d:
                d[start_x+1] = {} 
            if start_y not in d[start_x+1]:
                d[start_x+1][start_y] = 0

            if d[start_x+1][start_y]==1:
                min_val = min(min_val, abs(1000-(start_x+1)) + abs(1000-start_y))
            d[start_x+1][start_y]=2
            start_x += 1

        if c == 'L':
            if start_x-1 not in d:
                d[start_x-1] = {} 
            if start_y not in d[start_x-1]:
                d[start_x-1][start_y] = 0

            if d[start_x-1][start_y]==1:
                min_val = min(min_val, abs(1000-(start_x-1)) + abs(1000-start_y))
            d[start_x-1][start_y]=2
            start_x -= 1

        if c == 'U':
            if start_x not in d:
                d[start_x] = {} 
            if start_y+1 not in d[start_x]:
                d[start_x][start_y+1] = 0


            if d[start_x][start_y+1] == 1:
                min_val = min(min_val, abs(1000-start_x) + abs(1000-(start_y+1)))
            d[start_x][start_y+1]=2
            start_y += 1

        if c == 'D':
            if start_x not in d:
                d[start_x] = {} 
            if start_y-1 not in d[start_x]:
                d[start_x][start_y-1] = 0


            if d[start_x][start_y-1]==1:
                min_val = min(min_val, abs(1000-start_x) + abs(1000-(start_y-1)))
            d[start_x][start_y-1]=2
            start_y -= 1
print(min_val)
