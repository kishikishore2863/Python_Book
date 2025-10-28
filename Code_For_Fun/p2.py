#2. Using a loop, collect 10 shopping items as input. Use a Counter to count occurrences and display the most common item. If there’s a tie, display all tied items.

from collections import Counter

items = []
print("Enter 10 shopping items:")
for _ in range(10):
    items.append(input())

count = Counter(items)
max_count = max(count.values())
most_common = [item for item, cnt in count.items() if cnt == max_count]
print("Most common item(s):", most_common)


