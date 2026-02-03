#Write a recursive function to check whether a string is a palindrome.

def is_palindrome(s):
    # Base case: if the string has 0 or 1 characters, it's a palindrome
    if len(s) <= 1:
        return True

    # If first and last characters mismatch → not a palindrome
    if s[0] != s[-1]:
        return False

    # Recursive call on the substring without first & last characters
    return is_palindrome(s[1:-1])


# Example
# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))  # False

# def f(s):
#     start=0
#     end =len(s)-1
#     while start<end:
#         if s[start]!=s[end]:
#             return False
#         start = start+1
#         end = end-1
#
#     return True
#
# print(f("hello"))

def f1(s,start,end):
    if start>=end:
        return True

    if s[start] !=s[end]:
        return False

    return f1(s,start+1,end-1)
# s="hello"
s="aaa"
print(f1(s,0,len(s)-1))