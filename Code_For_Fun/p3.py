
#3. Read N words; use defaultdict(list) to group anagrams. Print only groups with size ≥ 3.

from collections import defaultdict

n = int(input("Enter number of words: "))
groups = defaultdict(list)

for _ in range(n):
    word = input()
    key = ''.join(sorted(word))
    groups[key].append(word)

for group in groups.values():
    if len(group) >= 3:
        print(group)

