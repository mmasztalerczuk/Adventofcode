d = {}


n1 = input().split(",")
n2 = input().split(",")

start_x = 1000
start_y = 1000
step = 1
for n in n1:
    c = n[0]
    v = int(n[1:])
    for i in range(1,v+1):
        
        if c == 'R':
            if start_x+1 not in d:
                d[start_x+1] = {}
            d[start_x+1][start_y]=step
            start_x += 1
        
        if c == 'L':
            if start_x-1 not in d:
                d[start_x-1] = {}
            d[start_x-1][start_y]=step
            start_x -= 1
        
        if c == 'U':
            if start_x not in d:
                d[start_x] = {}
            d[start_x][start_y+1]=step
            start_y += 1
        
        if c == 'D':
            if start_x not in d:
                d[start_x] = {}
            d[start_x][start_y-1]=step
            start_y -= 1
        
        step += 1

start_x = 1000
start_y = 1000
min_val = 1000000000000
step=1

for n in n2:
    c = n[0]
    v = int(n[1:])
    for i in range(1,v+1):
        if c == 'R':
            if start_x+1 not in d:
                d[start_x+1] = {} 
            if start_y not in d[start_x+1]:
                d[start_x+1][start_y]=0
            if d[start_x+1][start_y]!=0:
                min_val = min(min_val, d[start_x+1][start_y]+step)
            start_x+=1
        if c == 'L':
            if start_x-1 not in d:
                d[start_x-1] = {} 
            if start_y not in d[start_x-1]:
                d[start_x-1][start_y]=0
            if d[start_x-1][start_y]!=0:
                min_val = min(min_val, d[start_x-1][start_y]+step)
            start_x-=1
        if c == 'U':
            if start_x not in d:
                d[start_x] = {} 
            if start_y+1 not in d[start_x]:
                d[start_x][start_y+1]=0
            if d[start_x][start_y+1]!=0:
                min_val = min(min_val, d[start_x][start_y+1]+step)
            start_y+=1
        if c == 'D':
            if start_x not in d:
                d[start_x] = {} 
            if start_y-1 not in d[start_x]:
                d[start_x][start_y-1]=0
            if d[start_x][start_y-1]!=0:
                min_val = min(min_val, d[start_x][start_y-1]+step)
            start_y-=1
        step += 1

print(min_val)
