length = int(input("Enter room length (metres): "))
width = int(input("Enter room width (metres): "))
height = float(input("Enter room height (metres): "))

area = (length * height * 2) + (width * height * 2)

print(f"Wall area: {area:.2f} square metres")
print(f"Paint required: {area / 10:.1f} litres")