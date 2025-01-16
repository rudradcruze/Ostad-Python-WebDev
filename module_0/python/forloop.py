def multiplication_table(n):
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n * i))

def main():
    n = int(input("Enter a number: "))
    multiplication_table(n)

if __name__ == "__main__":
    main()