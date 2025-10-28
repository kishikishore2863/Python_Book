#6. Use deque to check if a string (ignore case and non-alphanumerics) is a palindrome by popping from both ends. Print TRUE/FALSE.
from collections import deque

s = input("Enter string: ")
filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
d = deque(filtered)

flag = True
while len(d) > 1:
    if d.popleft() != d.pop():
        flag = False
        break

print("TRUE" if flag else "FALSE")


