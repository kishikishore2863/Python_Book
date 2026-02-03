#Extract all palindromic words from a given list of words using list comprehensions
list_of_words = ["madam", "racecar","kishi","bob","king"]
palindrome = [ i for i in list_of_words if i==i[::-1] ]
print(palindrome)

