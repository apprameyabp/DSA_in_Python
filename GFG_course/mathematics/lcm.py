def find_lcm(a,b):
    return (a*b)//gcd(a,b)

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

print(find_lcm(4,6))