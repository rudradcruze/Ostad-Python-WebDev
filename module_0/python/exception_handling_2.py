while True:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    if n1 == 0 and n2 == 0:
        break

    try:
        print(int(n1) / int(n2))
    except ZeroDivisionError as e:
        print("You can't divide by zero")
        print(e)
    else:
        print("Good job!")