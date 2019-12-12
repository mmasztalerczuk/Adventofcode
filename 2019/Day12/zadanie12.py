class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def apply_gravity(self, other_moon):
        if self.x < other_moon.x:
            self.vel_x+=1
            other_moon.vel_x-=1
        elif self.x > other_moon.x:
            self.vel_x-=1
            other_moon.vel_x+=1

        if self.y < other_moon.y:
            self.vel_y+=1
            other_moon.vel_y-=1
        elif self.y > other_moon.y:
            self.vel_y-=1
            other_moon.vel_y+=1

        if self.z < other_moon.z:
            self.vel_z+=1
            other_moon.vel_z-=1
        elif self.z > other_moon.z:
            self.vel_z-=1
            other_moon.vel_z+=1                        

    def apply_vel(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

    def total_energy(self):
        #print(abs(self.x) + abs(self.y) +  abs(self.z))
        #print(abs(self.vel_x) +  abs(self.vel_y) +  abs(self.vel_z))
        return (abs(self.x) + abs(self.y) +  abs(self.z)) *(abs(self.vel_x) +  abs(self.vel_y) +  abs(self.vel_z))

    def compare_x(self, other_moon):
        if self.x == other_moon.x and self.vel_x == other_moon.vel_x:
            return True
        return False
    def compare_y(self, other_moon):
        if self.y == other_moon.y and self.vel_y == other_moon.vel_y:
            return True
        return False
    def compare_z(self, other_moon):
        if self.z == other_moon.z and self.vel_z == other_moon.vel_z:
            return True
        return False                  
moons = [Moon(12, 0, -15), 
            Moon(-8, -5, -10), 
            Moon(7, -17, 1), 
            Moon(2, -11, -6)]
org_moons = [Moon(12, 0, -15), 
            Moon(-8, -5, -10), 
            Moon(7, -17, 1), 
            Moon(2, -11, -6)]            
        
i = 0
f1, f2, f3 = False, False, False
a, b, c = 0, 0, 0
while True:
    #print()
    #print(f"After {i} steps")
    # for moon in moons:
    #     print(moon.x, moon.y, moon.z, ' ', moon.vel_x, moon.vel_y, moon.vel_z)
    for j in range(len(moons)):
        for k in range(j+1,len(moons)):
            moons[j].apply_gravity(moons[k])
    for moon in moons:
        moon.apply_vel()
    i+=1
    if not f1 and moons[0].compare_x(org_moons[0]) and moons[1].compare_x(org_moons[1]) and moons[2].compare_x(org_moons[2]) and moons[3].compare_x(org_moons[3]):
        f1 = True
        a = i
    if not f2 and moons[0].compare_y(org_moons[0]) and moons[1].compare_y(org_moons[1]) and moons[2].compare_y(org_moons[2]) and moons[3].compare_y(org_moons[3]):
        f2 = True
        b = i
    if not f3 and moons[0].compare_z(org_moons[0]) and moons[1].compare_z(org_moons[1]) and moons[2].compare_z(org_moons[2]) and moons[3].compare_z(org_moons[3]):
        f3 = True
        c = i                  
    #print(i)
    if f1 and f2 and f3:
        break
ans = 0
for moon in moons:
    ans += moon.total_energy()
    #print(ans)
print(a, b, c)

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

print(lcm(lcm(a, b), c))