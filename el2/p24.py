#Write a function to generate a multiplication table for a given number.
def table(n,k):
    if n == 0:
        return
    table(n-1,k)
    print(f"{k} * {n} = {k*n}")
print(table(10,5))