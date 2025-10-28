#5. Read Item(code, qty, price); compute bill total and print items where qty*price > threshold.

n = int(input("Enter number of items: "))
threshold = int(input("Enter threshold: "))
items = []

for _ in range(n):
    code = input("Item code: ")
    qty = int(input("Qty: "))
    price = int(input("Price: "))
    total = qty * price
    items.append((code, qty, price, total))

print("Items exceeding threshold:")
for item in items:
    if item[3] > threshold:
        print(item)


