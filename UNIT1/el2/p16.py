#Use filter() with a lambda to select prime numbers from a given list.
# from PlayGround.primeOrNot import isPrime

l=[1,2,3,4,5,6,7,8]
def isPrime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

r = list(filter(lambda x:isPrime(x),l))
print(r)