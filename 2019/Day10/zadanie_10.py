import sys
import math
asteroids = []
i = 0
for l in sys.stdin:
    j = 0
    for c in l[:-1]:
        if c == '#':
            asteroids.append((j,i))
        j += 1
    i += 1

# y = ax + b
# b = y - ax

# z = aw + y - ax
# z - y = aw - ax
#  z - y = a(w-x)
#  (z-y)/(w-x) = a
#print(asteroids)
ans = 0
for i in asteroids:
    s = set()
    d = {}
    tmp_ans = 0
    f1, f2, f3, f4 = True, True, True, True
    for j in asteroids:
        if j == i:
            continue
        a = 0
        b = 0
        if i[0]==j[0]:
            #print(f1, f2, i[1]>j[1], i, j)
            if i[1] > j[1] and f1:
                tmp_ans += 1
                f1 = False
            elif i[1] < j[1] and f2:
                tmp_ans += 1
                f2 = False
        elif i[1]==j[1]:

            if i[0] > j[0] and f3:
                tmp_ans += 1
                f3 = False
            elif i[0] < j[0] and f4:
                tmp_ans += 1
                f4 = False
        else:
            if i[0]-j[0] == 0:
                a = 0
            else:
                a = (i[1]-j[1])/(i[0]-j[0])
            b = i[1] - a * i[0]
            a = float(a)
            b = float(b)
            #print(i, j, (a, b))
            if (a,b) not in s:
                #print("ADD", (a,b))
                s.add((a,b))
                if i[1] > j[1]:
                    d[(a,b)] = 1
                else:
                    d[(a,b)] = -1
                #print('set', (a,b), ' on ', d[(a,b)])
            else:
                #print('test d',  d[(a,b)], i[1] < j[1])
                if d[(a,b)] > 0 and i[1] < j[1]:
                    tmp_ans += 1
                    d[(a,b)] = 0
                if d[(a,b)] < 0 and i[1] > j[1]:
                    tmp_ans += 1
                    d[(a,b)] = 0
                
        #print(i, j, (a,b), len(s)+tmp_ans)
    #print('fin', len(s) + tmp_ans)
    # print()
    # print()
    # print()
    # print()

    if ans < len(s) + tmp_ans:
        ans = len(s) + tmp_ans
        ans_s = s
        ans_i = i
    #print(i, ans, s)
#print(ans)
#print(ans_s)
print(ans_i)
#print(asteroids)
laser = []
i = ans_i
for a in asteroids:
    print(a)
    if a != ans_i:
        laser.append((a[0], a[1], (math.degrees(math.atan2(a[1]-i[1], a[0]-i[0]))+90+360)%360))
#print(laser)
laser_sorted = sorted(laser, key=lambda x: (x[2],abs(x[0]-i[0])+abs(x[1]-i[1])))
print(laser_sorted)
#
deg = -1
p = 0
r = 1
print('len', len(laser_sorted))
while len(laser_sorted) != 0:
    if len(laser_sorted) < p:
        p = 0
    if laser_sorted[p][2] != deg:
        deg = laser_sorted[p][2]
        print(r,laser_sorted[p])
        r += 1
        del laser_sorted[p]
    else:
        p += 1
        



# for a in range(len(laser_sorted)):
#     if laser_sorted[a][2] == 0:
#         break

# laser_sorted = laser_sorted[a:] + list(reversed(laser_sorted[:a]))
# print(laser_sorted)