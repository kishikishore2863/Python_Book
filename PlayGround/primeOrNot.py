
def isPrime(n):
    if n==1:
        return False
    res= False
    for i in range(2,n):
        if n%i ==0:
            break

    else:
        res= True
    return res

print(isPrime(8))