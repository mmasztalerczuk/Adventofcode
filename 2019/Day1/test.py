import sys


# PART I
#ans = 0

#for line in sys.stdin:
#    n = int(line)
#    ans += n//3 - 2
#print(ans)

#PART II

ans = 0
def calculate_fuel(fuel):
    return fuel//3 - 2

for line in sys.stdin:
    n = int(line)
    while True:
        tmp = calculate_fuel(n)
        if tmp <= 0:
            break
        else:
            ans += tmp
        n = tmp
print(ans)