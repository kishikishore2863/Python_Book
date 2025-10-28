#1. Write a Python program that uses a loop to count the frequency of each character in a given string using collections. Display only those characters whose frequency is greater than 2.

from collections import Counter

s = input("Enter a string: ")
freq = Counter(s)
for ch, count in freq.items():
    if count > 2:
        print(ch, "=", count)


