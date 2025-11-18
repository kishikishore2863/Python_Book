#Write a user-defined function that takes a string and returns its length.(Do not use len)
def length(s):
    if s == "":
        return 0
    return 1 + length(s[:-1])


print(length("kishore"))
