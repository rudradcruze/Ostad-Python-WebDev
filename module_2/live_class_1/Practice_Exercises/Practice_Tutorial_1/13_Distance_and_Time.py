distance = float(input("Enter distance in (km): "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

time = hours + (minutes / 60)
speed = distance / time

print(f"\nTime taken: {time:.2f} hours")
print(f"Average speed: {speed:.2f} km/h")