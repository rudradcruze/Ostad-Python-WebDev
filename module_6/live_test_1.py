# Live Test 1 - 06-03-2025
# Fibonacci Series
# Author: Francis Rudra D Cruze
# Author Email: francisrudra@gmail.com
# Gloabl Variables
fib_series = []

def fibonacci_by_terms(num_terms):

    a, b = 0, 1
    for _ in range(num_terms):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


def fibonacci_by_max_value(max_value):
    a, b = 0, 1
    while a <= max_value:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


def main():
    while True:
        print("=====================================")
        print("     Fibonacci Series Generator")
        print("=====================================")

        print("Author: Francis Rudra D Cruze")
        print("Author Email: francisrudra@gmail.com")
        print("Live Test: 1 - 06-03-2025")
        print("=====================================")

        print("\nChoose an option:\n1. Generate Fibonacci series by number of terms\n2. Generate Fibonacci series by maximum value\n3. Exit\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            num_terms = int(input("Enter the number of terms: "))
            if num_terms < 0:
                print("Number of terms should be a non-negative integer.")
                continue
            fib_series = fibonacci_by_terms(num_terms)
            print(f"Fibonacci series ({num_terms} terms): {', '.join(map(str, fib_series))}")
        elif choice == '2':
            max_value = int(input("Enter the maximum value: "))
            if max_value < 0:
                print("Maximum value should be a non-negative integer.")
                continue
            fib_series = fibonacci_by_max_value(max_value)
            print(f"Fibonacci series (up to {max_value}): {', '.join(map(str, fib_series))}")
        elif choice == '3':
            print("=====================================")
            print("\t      Exiting...")
            print("=====================================")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            continue


if __name__ == "__main__":
    main()