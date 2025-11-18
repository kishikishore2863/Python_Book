#Write a function to find LCM of two numbers using a helper function for GCD.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


x = 2
y = 4
print(lcm(x, y))