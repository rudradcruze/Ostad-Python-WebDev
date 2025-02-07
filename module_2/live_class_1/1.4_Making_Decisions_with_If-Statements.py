print("You find a mysterious door. What do you do?")
print("1. Open the door")
print("2. Knock first")
print("3. Walk away")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    print("The door creaks open...")
elif choice == "2":
    print("A friendly voice answers...")
elif choice == "3":
    print("You decide to play it safe...")
else:
    print("Invalid choice!")