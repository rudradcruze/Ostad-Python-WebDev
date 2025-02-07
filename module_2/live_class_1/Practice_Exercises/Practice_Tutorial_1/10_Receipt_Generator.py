shop_name = input("Enter store name: ")
item = []
price = []

for i in range(3):
    item.append(input("Enter item name: "))
    price.append(float(input("Enter price: ")))

print("======================================")
print(f"\t\t{shop_name.upper()}")
print("======================================")

for i in range(3):
    print(f"{item[i]}\t\t\t\t${price[i]:.2f}")

print("--------------------------------------")
print(f"Total\t\t\t\t${sum(price):.2f}")
print("======================================")