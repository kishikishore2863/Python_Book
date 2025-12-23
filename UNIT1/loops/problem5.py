# given number raed char by char

name = "kishore"
length = len(name)

for i in range(length):
    print(name[i])


name = "kishore"
reversed_name = name[::-1]
print("Reversed:", reversed_name)


name = "kishore"
vowels = "aeiou"
count = sum(1 for ch in name if ch.lower() in vowels)
print("Number of vowels:", count)


name = "kishore"
for i, ch in enumerate(name):
    print(f"Index {i} -> {ch}")


name = "kishore"
if name == name[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")