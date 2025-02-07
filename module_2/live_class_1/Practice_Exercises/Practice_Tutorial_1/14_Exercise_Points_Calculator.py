running = int(input("Minutes spent running: "))
swiming = int(input("Minutes spent swiming: "))
cycling = int(input("Minutes spent cycling: "))

print("\nPoints earned:")
print(f"Running: {running * 5} points")
print(f"Swimming: {swiming * 7} points")
print(f"Cycling: {cycling * 4} points")
print(f"Total: {(running * 5) + (swiming * 7) + (cycling * 4)} points")