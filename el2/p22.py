#Write a recursive function to count vowels in a string.
def count(s):
    if len(s)<1:
        return 0
    vowels="aeiou"
    if s[-1] in vowels:
        return 1+count(s[:-1])
    return 0+count(s[:-1])
print(count("kishore"))