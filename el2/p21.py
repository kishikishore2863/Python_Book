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
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False