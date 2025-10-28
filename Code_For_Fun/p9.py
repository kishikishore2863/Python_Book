#9. Write a function is_palindrome(word) that returns True if the string is palindrome (case insensitive).
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(is_palindrome("Madam"))
