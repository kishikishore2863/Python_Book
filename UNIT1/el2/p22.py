#Write a recursive function to count vowels in a string.
# def count(s):
#     if len(s)<1:
#         return 0
#     vowels="aeiou"
#     if s[-1] in vowels:
#         return 1+count(s[:-1])
#     return 0+count(s[:-1])
# print(count("kishore"))

def recursion(s,n,c):
    if n<1:
        return c

    if s[n] in "aeiou":
        c = c+1

    return recursion(s,n-1,c)

s="aaa kishore"
print(recursion(s,len(s)-1,0))
