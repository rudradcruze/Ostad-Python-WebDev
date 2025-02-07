import math

items = []

for i in range(5):
    items.append(float(input(f"Enter price for items {i+1}: ")))

print("Receipt Summary:")
sum = sum(items)

print(f"Total (rounded): ${round(sum)}")
print(f"Total (exact): ${sum:.2f}")
print(f"Average per item (rounded): ${round(sum/5)}")
print(f"Average per item (exact): ${sum/5}")