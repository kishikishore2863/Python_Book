#4. Read N integers; build OrderedDict to keep first occurrence only. Print unique sequence preserving input order.

from collections import OrderedDict

n = int(input("Enter count: "))
unique = OrderedDict()

for _ in range(n):
    num = int(input())
    if num not in unique:
        unique[num] = 1

print(list(unique.keys()))

