#15. Create three functions Functions:is_prime(n), is_perfect(n), is_armstrong(n) Ask user for a number and classify which types apply
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    s = sum(int(d)**3 for d in str(n))
    return s == n

num = int(input("Enter a number: "))
print("Prime:", is_prime(num))
print("Perfect:", is_perfect(num))
print("Armstrong:", is_armstrong(num))

