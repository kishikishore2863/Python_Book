#8. Define count_vowels(text) that counts and returns the number of vowels in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

print(count_vowels("Hello World"))


